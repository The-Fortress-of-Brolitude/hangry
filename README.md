# hangry
## When people get hungry they often get angry. Be happy, not hangry.

* Input Yelp API tokens in a file named 'config.ini' in the following format
* Hangry runs as a Flask app on port 5000 by default

```
[yelp_api]
CONSUMER_KEY: your_consumer_key
CONSUMER_SECRET: your_consumer_secret
TOKEN: your_token
TOKEN_SECRET: your_token_secret
```

```
usage: hangry.py [-h] [-q TERM] [-l LOCATION]

optional arguments:
  -h, --help            show this help message and exit
  -q TERM, --term TERM  Search term (default: dinner)
  -l LOCATION, --location LOCATION
                        Search location (default: Fairfax, VA)
```