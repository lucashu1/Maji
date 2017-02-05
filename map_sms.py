from flask import Flask, request
from twilio import twiml
from arcgis.gis import GIS

# control program flow
# 0: not initialized
# 1: received location
# 2: received source name, display status
state = 0;
location = ''

locations = {
	"LOS ANGELES" : 
	{
		"Marina del Rey" : "Clean",
		"Venice" : "Dirty",
		"Santa Monica" : "Dirty"
	},
	"MICHIGAN" : 
	{
		"Flint" : "Dirty",
		"Lake Michigan" : "Clean"
	}
}

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms():
	global state
	global locations
	global location

	number = request.form['From']
	message_body = request.form['Body']

	resp = twiml.Response()

	if state == 0:
		resp.message('Hello {}, text us your city, town, or village to initialize Maji'.format(number))
		state = 1

	elif state == 1:
		
		if message_body.upper() in locations.keys():
			location = message_body.upper()
			resp.message('You said you are in: {}'.format(location))
			resp.message('Message \'STATUS\' to get water information')
			state = 2
		
		else:
			resp.message('Location not valid! Please try again')

	elif state == 2 and "STATUS" in message_body.upper():
		for source, state in locations[location].items():
			resp.message('Water source: {}. Status: {}'.format(source, state))
		resp.message('Thank you for using Maji! Text us any message to use Maji again.')
		state = 0;

	elif state >= 3:
		resp.message('You have reached the end of this demo')

	else:
		resp.message('Uh oh! Something\'s wrong.')
	
	return str(resp)

if __name__ == "__main__":
	app.run()