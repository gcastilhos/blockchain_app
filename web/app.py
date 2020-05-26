"""
Main Module for Blockchain1
"""
import os
from random import randint
from flask import Flask, render_template, request, jsonify
from bchain.bchain import create_block, create_hash, create_block_chain
app = Flask(__name__)


NONCE = '23df'
FIRST_HASH = ("0000100308e7e0bea95a3e88e4e406c3"
              "7133f0929c80866bda04bc0bce53a15")
TITLE = 'Blockchain1'
INITIAL_BLOCK_NO = 432


@app.route("/")
def index():
    return create_data(2)


@app.route("/eventdata")
def event_data():
    return create_block()


@app.route("/hash")
def hashcode():
    nonce, hash_code = create_hash(request)
    return jsonify(nonce, hash_code)


@app.route("/houses")
def houses():
    return create_data(7)


def create_data(number_of_hash_codes):
    """Generate the data for the espeficied number of hash codes,
    plus the previous code. For one house, the number of hash codes
    should be 2, for 2, should be 3, and so on.
    """
    nonces, hash_codes = zip(*create_block_chain(FIRST_HASH, NONCE))
    params = {'title': TITLE,
              'block_no': INITIAL_BLOCK_NO,
              'event_data': [create_block()] * number_of_hash_codes,
              'nonce_list': nonces[:number_of_hash_codes],
              'hash_list': hash_codes[:number_of_hash_codes],
              'production': os.environ.get('PRODUCTION', False),
              'size': number_of_hash_codes,
              }
    return render_template('houses.html', **params)



