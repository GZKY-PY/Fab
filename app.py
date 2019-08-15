# coding=utf-8
from flask import Flask


import os

app = Flask(__name__)

@app.route('/')
def hello():
	
	return "Hello World! i have been seen 不知道 times."

app.run(host="0.0.0.0",debug=True)
