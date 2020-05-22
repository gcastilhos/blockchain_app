"""
Main Module for Blockchain1
"""
from flask import Flask, render_template, request, make_response
app = Flask(__name__)


@app.route("/")
def index():
    message = 'Blockchain1'
    return render_template('index.html', message=message)
