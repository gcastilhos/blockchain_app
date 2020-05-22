"""
Main Module for Blockchain1
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "Blockchain1"
