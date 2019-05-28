#!venv/bin/python
#from xd import app, db
import requests

import os
from flask import Flask, request, jsonify
app = Flask(__name__)

geocode_key = "55f25fb5440fbf37dd545534ddd53ee5d43e2b2"
zomato_key = "05fb51eb0e4d27b795abe3910420f06a"

@app.route('/')
def hello():
    return "hello world"

if __name__ == '__main__':
    app.run(debug=True)



