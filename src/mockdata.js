const MOCK_EVENT_DATA = "Date|Time|EventID|Appl.ID |ActivePWR |ReactivePwr|Voltage|Intensity |HASH\u003e\u003e\u003e 10Mar2015 0:00:00 1201210 9b75a5178a 2.58 0.136 241.97 10.6\u003e\u003e\u003e 10Mar2015 0:01:00 1201211 9b75a5178f 2.552 0.1 241.75 10.4\u003e\u003e\u003e 10Mar2015 0:02:00 1201212 9b75a51791 2.55 0.1 241.64 10.4\u003e\u003e\u003e 10Mar2015 0:03:00 1201213 9b75a5178d 2.55 0.1 241.71 10.4\u003e\u003e\u003e 10Mar2015 0:04:00 1201214 9b75a5178b 2.554 0.1 241.98 10.4\u003e\u003e\u003e 10Mar2015 0:05:00 1201215 9b75a5178f 2.55 0.1 241.83 10.4\u003e\u003e\u003e 10Mar2015 0:06:00 1201216 9b75a51790 2.534 0.09 241.07 10.4\u003e\u003e\u003e 10Mar2015 0:07:00 1201217 9b75a51791 2.484 0.21 241.29 10.2\u003e\u003e\u003e 10Mar2015 0:08:00 1201218 9b75a5178a 2.468 0.32 241.23 10.2\u003e\u003e\u003e 10Mar2015 0:09:00 1201219 9b75a51793 2.48 0.54 242.28 10.2";

const INITIAL_HASH = "0";

const MOCK_DATA = {
  columns: [
    'Event_Id',
    'Date',
    'Time_24H',
    'Duration_Min',
    'Appl_Id',
    'Appl.NAME',
    'Global_active_power',
    'Global_reactive_power',
    'Voltage',
    'Global_intensity',
    'Total Subm. 1+2+3',
    'Total measum. WH',
    'POWER Composition [kWH]',
    'USE CATEG',
    'CATEGORY NAME (Literal)'
  ],
  data: [
    [
      40979,
      '11/07/2020',
      '18:49:45',
      2,
      '0006_c2',
      'PC1_Gar',
      2.69,
      0.09,
      248.75,
      11.45,
      22,
      44,
      0.04,
      'E',
      'EDUCATION, COMMS, ENTERNTAINMENT'
    ]
  ]
};

export {MOCK_DATA, MOCK_EVENT_DATA, INITIAL_HASH}
