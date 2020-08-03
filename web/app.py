"""
Main Module for Blockchain1
"""
import os
from flask import Flask, render_template, request, jsonify
from flask_talisman import Talisman, DEFAULT_CSP_POLICY
from bchain.bchain import create_hash, create_data, create_block
app = Flask(__name__)
Talisman(app,
         content_security_policy=os.environ.get('CSP_DIRECTIVES',
                                                DEFAULT_CSP_POLICY),
         content_security_policy_nonce_in=['script-src'])
from web.queue_manager import event_generator
queue_events = event_generator()
from web.generator_lock import GeneratorLock
generator = GeneratorLock(queue_events)

if os.environ.get('TEST_ENV'):
    from flask_cors import CORS
    cors = CORS(app, resources={r"/events": {"origins": "http://localhost:8080"},
                                r"/hash": {"origins": "http://localhost:8080"}})


@app.route("/")
def index():
    return render_template('houses.html', **create_data(1))


@app.route("/eventdata")
def event_data():
    return create_block()


@app.route("/hash")
def hashcode():
    nonce, hash_code = create_hash(request)
    return jsonify(nonce, hash_code)


@app.route("/houses")
def houses():
    return render_template('houses.html', **create_data(6))


@app.route("/events")
def events():
    event = None
    while event is None:
        try:
            event = generator.next()
        except ValueError as error:
            print(error)
    return app.response_class(response=event, mimetype='application/json')
