"""
Main Module for Blockchain1
"""
from flask import Flask, render_template, request, make_response
app = Flask(__name__)


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
LINE_BREAK = "<br />"

@app.route("/")
def index():
    message = 'Blockchain1'
    return render_template('index.html', message=message)


@app.route("/message")
def message():
    return create_block()


def create_block():
    data = [DATA_HEADER]
    records = [f">>> {rec}" for rec in DATA_RECORDS]
    return LINE_BREAK.join(data + records)
