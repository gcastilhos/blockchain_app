"""
Main Module for Blockchain1
"""
import os
from random import randint
from flask import Flask, render_template, request, jsonify
from flask_talisman import Talisman, DEFAULT_CSP_POLICY
from bchain.bchain import create_hash, create_data
app = Flask(__name__)
Talisman(app,
         content_security_policy=os.environ.get('CSP_DIRECTIVES',
                                                DEFAULT_CSP_POLICY),
         content_security_policy_nonce_in=['script-src'])


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

