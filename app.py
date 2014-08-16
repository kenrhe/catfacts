from flask import Flask, render_template, request, session, redirect, jsonify
import jinja2
import os
import hashlib

import datetime
import pymongo
import random

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
	try:
		doc_count = facts_db.count()
		col_index = random.randint(0, doc_count)
		return render_template("index.html", facts=facts_db.find()[col_index]['facts'])
	except Exception, e:
		print "[EXCEPTION ERROR] " + e

@app.route('/send', methods=['POST'])
def send():
	if request.method == 'POST':
		pass

@app.route('/create', methods=['GET','POST'])
def create():
	if request.method == 'POST':
		try:
			if request.form['submit'] == 'create':
				fact_list = {'name':request.form['list']}
				facts_db.insert(fact_list);
			elif request.form['submit'] == 'add':
				list_name = request.form['list']
				fact = request.form['fact']
				facts_db.update({'name':list_name}, {'$push': {'facts':fact}}, True)
			return redirect('/create')
		except Exception, e:
			print "[EXCEPTION ERROR] " + e
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