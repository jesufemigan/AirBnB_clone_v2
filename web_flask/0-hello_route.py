#!/usr/bin/python3
'''A falsk web app'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


app.run()
