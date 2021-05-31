from flask import Flask
import dill
import pandas as pd
import os
dill._dill._reverse_typemap['ClassType'] = type

app = Flask(__name__)
model = None


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
