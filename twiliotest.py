from twilio.rest import TwilioRestClient

account_sid = "ACd26f82b355704979597403975eae09e4"
auth_token = "4dfdd50a80fa3f5d5ad987c7fb472ae0"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python!",
	to="+18582274815",
	from_="+18583488942")

client.messages.create(
	to="+18582274815",
	from_="+18583488942",
	body="This is the ship that made the Kessel Run in fourteen parsecs",
	media_url="https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg")

print(message.sid)