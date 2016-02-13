import argparse
import ConfigParser
from config import ConfigSectionMap

Config = ConfigParser.ConfigParser()
Config.read("config.ini")

API_HOST = 'api.yelp.com'
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'Fairfax, VA'
SEARCH_LIMIT = 3
SEARCH_PATH = '/v2/search/'
BUSINESS_PATH = '/v2/business'

# OAuth credential placeholders that must be filled in by users.
CONSUMER_KEY = ConfigSectionMap("yelp_api")['consumer_key']
CONSUMER_SECRET = ConfigSectionMap("yelp_api")['consumer_secret']
TOKEN = ConfigSectionMap("yelp_api")['token']
TOKEN_SECRET = ConfigSectionMap("yelp_api")['token_secret']

input_values = parser.parse_args()

try:
    query_api(input_values.term, input_values.location)
except urllib2.HTTPError as error:
    sys.exit(
        'Encountered HTTP error {0}. Abort program.'.format(error.code))

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--term', dest='term', default=DEFAULT_TERM,
                        type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--location', dest='location',
                        default=DEFAULT_LOCATION, type=str,
                        help='Search location (default: %(default)s)')

    input_values = parser.parse_args()

if __name__ == '__main__':
    main()