
# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
from serialize.py import TripSerializer


# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC7f33789db90afa45749656926700a7f1"
auth_token  = "63a1850c200e719d08c0d0c343d47e54"
client = TwilioRestClient(account_sid, auth_token)


sms = client.sms.messages.create(body="Jenny please?! I love you <3",
    to="+14159352345",
        from_="+14158141829")
	print sms.sid
