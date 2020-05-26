"""
Main Module for Blockchain1
"""
from random import randint
from flask import Flask, render_template, request, jsonify
from bchain.bchain import create_hash, create_data
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('houses.html', **create_data(2))


@app.route("/eventdata")
def event_data():
    return create_block()


@app.route("/hash")
def hashcode():
    nonce, hash_code = create_hash(request)
    return jsonify(nonce, hash_code)


@app.route("/houses")
def houses():
    return render_template('houses.html', **create_data(7))

