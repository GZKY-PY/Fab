# coding=utf-8
from flask import Flask
from redis import Redis

import os
redis_client = Redis(host="localhost",port=6379)

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello World!"

app.run(host="0.0.0.0",debug=True)
