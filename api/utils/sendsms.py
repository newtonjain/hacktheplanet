from twilio.rest import TwilioRestClient
import environ
env = environ.Env()

account_sid = env("ACCOUNT_SID", default="")
auth_token = env("AUTH_TOKEN", default="")
client = TwilioRestClient(account_sid, auth_token)


class SMS(object):

    def __init__(self, number):
        """ Initilializes SMS  """
        self.number = "+" + str(number)

    def send(self, body_text):
        """ Sends SMS """
        message = client.sms.messages.create(body=str(body_text), to=self.number, from_="+13853557433")
        return message.sid
