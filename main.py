import json
import os
#import stripe
#import smtplib
import requests

from flask import Flask, request, jsonify

app= Flask(__name__)

@app.route('/')
def hello():
	print("This is main page!")
	return "Hello World!"

@app.route('/run_post')
def run_post():
	print("This is Run Post.")
	url = ('https://linebot-testing-python.herokuapp.com/stripetest')
	data={'stripeAmount':'199',
		'stripeCurrency':'USD',
		'stripeToken':'122',
		'stripeDescription':'Test post'
		}
	headers={'Content-Type':'application/json'}
	print ("Request -------*******")
	r = requests.post(url, data=json.dumps(data), headers=headers)
	print r.json
	print ("Responds --------******")
	print r.text
	return "HEY!"

if __name__ == "__main__" :
    app.run()