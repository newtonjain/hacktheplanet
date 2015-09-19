import json
import urllib
import urllib2
import environ
env = environ.Env()

import oauth2

API_HOST = 'api.yelp.com'
DEFAULT_TERMS = ['landmarks', 'parks', 'hiking']
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 5
SEARCH_PATH = '/v2/search/'

CONSUMER_KEY = env("CONSUMER_KEY", default="")
CONSUMER_SECRET = env("CONSUMER_SECRET", default="")
TOKEN = env("TOKEN", default="")
TOKEN_SECRET = env("TOKEN_SECRET", default="")


class Yelp(object):

    def __init__(self):
        pass

    def request(self, url_params=None):
        url_params = url_params or {}
        url = 'http://{0}{1}?'.format(API_HOST, urllib.quote(SEARCH_PATH.encode('utf8')))

        consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        oauth_request = oauth2.Request(method="GET", url=url, parameters=url_params)

        oauth_request.update(
            {
                'oauth_nonce': oauth2.generate_nonce(),
                'oauth_timestamp': oauth2.generate_timestamp(),
                'oauth_token': TOKEN,
                'oauth_consumer_key': CONSUMER_KEY
            }
        )
        token = oauth2.Token(TOKEN, TOKEN_SECRET)
        oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
        signed_url = oauth_request.to_url()

        print(u'Querying {0} ...'.format(url))

        conn = urllib2.urlopen(signed_url, None)
        try:
            response = json.loads(conn.read())
        finally:
            conn.close()

        return response

    def get_locations(self):
        '''Get locations based on search terms and location.'''
        terms = ''
        for term in DEFAULT_TERMS:
            terms.append(term + ',')
        url_params = {
            'term': terms,
            'location': DEFAULT_LOCATION.replace(' ', '+'),
            'limit': SEARCH_LIMIT
        }
        return self.request(url_params=url_params)
