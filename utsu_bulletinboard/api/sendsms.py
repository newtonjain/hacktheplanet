
# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
account_sid = "AC7f33789db90afa45749656926700a7f1"
auth_token  = "63a1850c200e719d08c0d0c343d47e54"
client = TwilioRestClient(account_sid, auth_token)


class SMS(object):
    def __init__(self, number, message):
    """ Initilializes SMS  """
      	self.number = "+" + number
	self.message = message

    def send(self):
    """ Sends SMS """
    	client.sms.messages.create(body=self.message, to=self.number, from_="+13853557433")
	return sms.sid
