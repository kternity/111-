#!/usr/bin/evn python3
# -*- coding: uft8 -*-
"""Sample hello world Flask app"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
   return "<h1>Hello, world!</h1>"
   