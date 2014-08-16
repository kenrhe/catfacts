from flask import Flask, render_template, request, session, redirect, jsonify
import jinja2
import os
import hashlib

import datetime
import pymongo

from pymongo import MongoClient
from twilio.rest import TwilioRestClient

ACCOUNT_SID = "ACcf72ea65363c8e7585acf4ae877b49ab"
AUTH_TOKEN = "e61112fee5d7c53cf5983ed9f5c97115"
FROM_NUMBER = "+12015618743"

app = Flask(__name__)

MONGO_URL = os.environ.get('MONGOHQ_URL')
client = MongoClient(MONGO_URL)
db = client.app28556815
users_db = db.users
facts_db = db.facts

@app.route('/')
def index():
	#send_message('2012500807', 'Ken is so sexy.')
	return render_template("index.html")

@app.route('/create', methods=['GET','POST'])
def create():
	if request.method == 'POST':
		list_name=request.form['list']
		fact=request.form['fact']

		facts_db.update({'name':list_name}, {'$push' : {fact}})
		return redirect('/create')
	return render_template('create.html')

def send_message(to_number, body_message):
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        to = to_number,
        from_= FROM_NUMBER,
        body= body_message
    )
	
if __name__ == '__main__':
	#this code starts the web app, it can be found at http://localhost:8000
	port = int(os.environ.get('PORT', 8000))
	app.run(host='0.0.0.0', port=port,debug=True)