"""
Main Module for Blockchain1
"""
from flask import Flask, render_template, request, jsonify
from bchain.bchain import create_block, create_hash
app = Flask(__name__)


@app.route("/")
def index():
    params = {'message': 'Blockchain1',
              'block_no': "000432",
              'event_data': create_block(),
              }
    return render_template('index.html', **params)


@app.route("/eventdata")
def event_data():
    return create_block()


@app.route("/hash")
def hashcode():
    nonce, hash_code = create_hash(request)
    return jsonify((hex(nonce).replace("0x", ''), hash_code))


@app.route("/houses")
def houses():
    params = {'message': 'Blockchain1',
              'block_no': "000432",
              'event_data': create_block(),
              }
    return render_template('houses.html', **params)
