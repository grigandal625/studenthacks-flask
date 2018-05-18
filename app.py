# -*- coding: utf-8 -*- 

import os

from flask import Flask, render_template, redirect, url_for, json, request
import requests

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/', methods=['GET'])
def index():
	import datetime
	dt = datetime.datetime.now()
	import time
	response = str(time.mktime(dt.timetuple()))
	response = response[0:-1]
	response = response[0:-1]
	return response
