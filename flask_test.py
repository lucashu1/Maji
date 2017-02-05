from flask import Flask, request
from twilio import twiml

# control program flow
# 0: not initialized
# 1: received location
# 2: received source name, display status
state = 0;

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms():
	global state

	number = request.form['From']
	message_body = request.form['Body']

	resp = twiml.Response()

	if state == 0:
		resp.message('Hello {}, text us your city to initialize Maji'.format(number))
		state = 1

	elif state == 1:
		resp.message('You said you are in: {}'.format(message_body))
		resp.message('Message \'[SOURCE NAME] status\' to get water information')
		state = 2

	elif state == 2 and "status" in message_body:
		if "Venice" in message_body or "venice" in message_body:
			resp.message('State of {}: {}'.format('Venice', 'DIRTY'))
		elif "Marina" in message_body or "marina" in message_body:
			resp.message('State of {}: {}'.format('Marina Del Rey', 'CLEAN'))

	elif state >= 3:
		resp.message('You have reached the end of this demo')

	else:
		resp.message('Uh oh! Something\'s wrong.')
	
	return str(resp)

if __name__ == "__main__":
	app.run()