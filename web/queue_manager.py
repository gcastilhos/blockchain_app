# coding: utf-8
import os
import pandas as pd
from datetime import datetime, timedelta
from functools import partial
import pickle
from random import randint


def event_generator():
    data_set = fetch_data_set()
    columns = get_columns(data_set.dtypes)
    position = 0
    alternating_factor = 1
    while True:
        factor, position = reset_position(position, data_set)
        records = data_set.iloc[position:position + 1].copy()
        position += factor + 1 
        update_values(records, alternating_factor * factor, columns)
        alternating_factor = -alternating_factor
        yield records.to_json(index=False, orient="split")


def fetch_data_set():

    def date_offset(min_date, a_date):
        offset_date = datetime.date(datetime.now()) + (datetime.date(a_date) - min_date)
        return datetime.strftime(offset_date, "%d/%m/%Y")

    def change_dates():
        data_set.Date = pd.to_datetime(data_set.Date)
        min_date = datetime.date(data_set.Date.min()) 
        dt_offset = partial(date_offset, min_date)
        data_set.Date = data_set.Date.apply(dt_offset)

    data_set = pickle.load(open(os.path.join(os.environ['QUEUE_DATA'], 'appliances_list.pickle'), 'rb'))
    change_dates()
    return data_set


def get_columns(data_types):
    return [(key, val) for key, val in data_types.to_dict().items() if key != 'Event_Id' and val != 'object']


def reset_position(position, data_set):
    factor = randint(4, 10)
    if position + factor > data_set.shape[0]:
        position = 0
        data_set.Event_Id = data_set.Event_Id + data_set.Event_Id.max() - data_set.Event_Id.min() + 1
    return factor, position
 

def update_values(records, factor, columns):
    multiplier = 1 + factor / 100
    for col, dtype in columns:
        records.loc[:, col] = records.loc[:, col].apply(lambda val: round(val * multiplier, 2) if dtype == 'float64' else int(val * multiplier))


if __name__ == '__main__':
    events = event_generator()
    while True:
        print(next(events))
        try:
            input("Press ENTER to continue or CTRL-D to stop")
        except KeyboardInterrupt:
            pass
        except EOFError:
            print("\nSimulation terminated")
            break
