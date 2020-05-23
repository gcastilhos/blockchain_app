"""
Main Module for Blockchain1
"""
import logging
import html
from hashlib import sha256
from urllib.parse import urlparse, parse_qsl
from flask import Flask, render_template, request, make_response
app = Flask(__name__)

logger = logging.getLogger(__name__)
fh = logging.FileHandler(f'{__name__}.log')
logger.addHandler(fh)
logger.setLevel(logging.INFO)


DATA_HEADER = "Date|Time|EventID|Appl.ID |ActivePWR |ReactivePwr|Voltage|Intensity |HASH" 
DATA_RECORDS = ["10Mar2015 0:00:00 1201210 9b75a5178a 2.58 0.136 241.97 10.6",
               "10Mar2015 0:01:00 1201211 9b75a5178f 2.552 0.1 241.75 10.4",
               "10Mar2015 0:02:00 1201212 9b75a51791 2.55 0.1 241.64 10.4",
               "10Mar2015 0:03:00 1201213 9b75a5178d 2.55 0.1 241.71 10.4",
               "10Mar2015 0:04:00 1201214 9b75a5178b 2.554 0.1 241.98 10.4",
               "10Mar2015 0:05:00 1201215 9b75a5178f 2.55 0.1 241.83 10.4",
               "10Mar2015 0:06:00 1201216 9b75a51790 2.534 0.09 241.07 10.4",
               "10Mar2015 0:07:00 1201217 9b75a51791 2.484 0.21 241.29 10.2",
               "10Mar2015 0:08:00 1201218 9b75a5178a 2.468 0.32 241.23 10.2",
               "10Mar2015 0:09:00 1201219 9b75a51793 2.48 0.54 242.28 10.2",
               ]
LINE_BREAK = ""

@app.route("/")
def index():
    params = {'message': 'Blockchain1',
              'nonce': "f34b32da", 
              'block_no': "000432",
              'event_data': create_block(),
              }
    return render_template('index.html', **params)


@app.route("/eventdata")
def event_data():
    return create_block()


def create_block():
    data = [DATA_HEADER]
    records = [f">>> {rec}" for rec in DATA_RECORDS]
    return LINE_BREAK.join(data + records)


@app.route("/hash")
def hash():
    return create_hash(request)


def create_hash(request):
    encoder = sha256()
    params = dict(parse_qsl(request.query_string))
    values = params.get(b'block_no', b'') + params.get(b'eventData', b'') + \
             params.get(b'nonce', b'')
    encoder.update(values)
    logger.info("Hash values: %s, %s, %s", *params.values())
    return encoder.hexdigest()
