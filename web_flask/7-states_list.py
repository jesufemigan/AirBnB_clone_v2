#!/usr/bin/python3
'''a flask web app that lists all states'''

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    '''definition for /states_list'''
    all_states = storage.all(State)
    data = {'states': all_states}
    return render_template("7-states_list.html", data=data)


@app.teardown_appcontext
def close_sql():
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
