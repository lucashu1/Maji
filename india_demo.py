from flask import Flask, request
from twilio import twiml
from arcgis.gis import GIS

# state controls program flow
# stateLoc is location descriptor

state = 0;
gps = False
country = ''
stateLoc = ''
district = ''
town = ''
location = ''
message_text = ''

locations = {
	"INDIA" : 
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

	global gps
	global state

	global country
	global stateLoc
	global district
	global town
	global location

	number = request.form['From']
	message_body = request.form['Body']

	resp = twiml.Response()

	if state == 0:
		resp.message('Hello {}, welcome to Maji. I noticed your phone doesn\'t support GPS. Can you tell me where you are?'.format(number))
		if "YES" in message_body.upper():
			gps = true
		elif "NO" in message_body.upper():
			gps = false
		state = 1

	elif state == 1:
		resp.message('What country are you in?')
		country = message_body.upper()
		state = 2

	elif state == 2:
		if message_body.upper() in 'INDIA':
			resp.message('What state of India are you in?')
			state = 3
		else:
			resp.message('Seems like you made a typo. Please try again.')
		stateLoc = message_body.upper()

	elif state == 3:
		if message_body.upper() in 'ANDHRA PRADESH':
			resp.message('What district of Andhra Pradesh are you in?')
			state = 4
		else:
			resp.message('Seems like you made a typo. Please try again.')
		district = message_body.upper()

	elif state == 4:
		if message_body.upper() in "GUNTUR":
			resp.message('What town/village of Guntur are you in?')
			state = 5
		else:
			resp.message('Seems like you made a typo. Please try again.')
		town = message_body.upper()

	elif state == 5:
		if message_body.upper() in 'THULLUR':
			resp.message('Here are some landmarks that other Maji users have pinned in Thullur:\nVeera Temple\nGvmt hospital\nBible Mission Church\nThullur Library\nWhich of these landmarks are you closest to?')
			
			state = 6
		else:
			resp.message('Seems like you made a typo. Please try again.')
		location = message_body.upper()

	elif state == 6:
		if message_body.upper() in "THULLUR LIBRARY":
			resp.message('Reply WATER to get local water information')
			state = 7
		else:
			resp.message('Seems like you made a typo. Please try again.')

	elif state == 7:
		if message_body.upper() in "WATER":
			
			resp.message('Here are the water sources near Thullur Library:\nSource: THULLURU LAKE. Status: DO NOT DRINK\nSource: HAND PUMP. Status: QUESTIONABLE\nSource: NORTH WELL. Status: DO NOT DRINK\nSource: SOUTH WELL. Status: SAFE TO DRINK\n')
			
			resp.message('Nearest clean source: NORTH WELL\nLocation: .4km north of Thullur Library\nLast updated: 17 Jan 2017 by UNICEF at 0900hrs\nWould you like to see directions from Thullur Library to NORTH WELL?')
			
			state = 8

		else:
			resp.message('Seems like you made a typo. Please try again.')

	elif state == 8:
		if message_body.upper() in "NO":
			resp.message('Ok.')
		else:
			resp.message('Resetting Maji!')
			state = 0
			
	else:
		resp.message('Uh oh! Something\'s wrong.')
	
	return str(resp)

if __name__ == "__main__":
	app.run()