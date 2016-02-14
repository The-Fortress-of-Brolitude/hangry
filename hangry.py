import argparse
import configparser
import requests
import oauth2 as oauth
import pprint
from requests_oauthlib import OAuth1Session
from flask import Flask

app = Flask(__name__)

Config = configparser.ConfigParser()
Config.read("config.ini")

API_HOST = 'https://api.yelp.com'
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'Fairfax, VA'
SEARCH_LIMIT = 3
SEARCH_PATH = '/v2/search/'
BUSINESS_PATH = '/v2/business'

# OAuth credential placeholders that must be filled in by users.
CONSUMER_KEY = Config["yelp_api"]['consumer_key']
CONSUMER_SECRET = Config["yelp_api"]['consumer_secret']
TOKEN = Config["yelp_api"]['token']
TOKEN_SECRET = Config["yelp_api"]['token_secret']

def request(host, path, url_params=None):
    """Format a proper OAuth request to the API"""

    url_params = url_params or {}
    url = host + path

    yelp = OAuth1Session(
        CONSUMER_KEY,
        client_secret=CONSUMER_SECRET,
        resource_owner_key=TOKEN,
        resource_owner_secret=TOKEN_SECRET)

    print u'Querying Yelp API...'

    response = yelp.get(url, params=url_params)
    return response.json()

def search(term, location):
    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, SEARCH_PATH, url_params=url_params)

def query_api(term, location):
    response = search(term, location)

    pprint.pprint(response, indent=2)

@app.route('/')
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--term', dest='term', default=DEFAULT_TERM,
                        type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--location', dest='location',
                        default=DEFAULT_LOCATION, type=str,
                        help='Search location (default: %(default)s)')

    input_values = parser.parse_args()

    query_api(input_values.term, input_values.location)

if __name__ == '__main__':
    app.run()