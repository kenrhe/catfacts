from twilio.rest import TwilioRestClient 

ACCOUNT_SID = "ACcf72ea65363c8e7585acf4ae877b49ab" 
AUTH_TOKEN = "e61112fee5d7c53cf5983ed9f5c97115" 
FROM_NUM = "+12015618743"

def send_message(TO_NUM, BODY):
 
	# put your own credentials here 
	 
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
	 
	client.messages.create(
		to = TO_NUM, 
		from_= FROM_NUM, 
		body= BODY  
	)