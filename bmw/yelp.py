import environ
env = environ.Env()
from yelpapi import YelpAPI

API_HOST = 'api.yelp.com'
DEFAULT_TERMS = 'landmarks,parks,hiking,lakes,golf,boating'
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 5
SEARCH_PATH = '/v2/search/'

CONSUMER_KEY = env("CONSUMER_KEY", default="")
CONSUMER_SECRET = env("CONSUMER_SECRET", default="")
TOKEN = env("TOKEN", default="")
TOKEN_SECRET = env("TOKEN_SECRET", default="")


class Yelp(object):

    def __init__(self, longitude, latitude):
        self.client = YelpAPI(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)
        self.longitude = str(longitude)
        self.latitude = str(latitude)

    def get_locations(self):
        return self.client.search_query(
            ll=self.latitude + ',' + self.longitude,
            limit=5,
            category_filter=DEFAULT_TERMS,
            radius_filter=100)
