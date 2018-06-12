from os import environ

config = {
    'SECRET_KEY': environ['SECRET_KEY'],
#    'SERVER_NAME': f"auth.{environ['DOMAIN_ROOT']}",
    'SQLALCHEMY_DATABASE_URI': environ['DATABASE_URL'],
    'AUTH_GOOGLE': {
        'consumer_key': environ['GOOGLE_CONSUMER_KEY'],
        'consumer_secret': environ['GOOGLE_CONSUMER_SECRET'],
    },
    'AUTH_TWITTER': {
        'consumer_key': environ['TWITTER_CONSUMER_KEY'],
        'consumer_secret': environ['TWITTER_CONSUMER_SECRET'],
    },
    'AUTH_GITHUB': {
        'consumer_key': environ['GITHUB_CONSUMER_KEY'],
        'consumer_secret': environ['GITHUB_CONSUMER_SECRET'],
    }
}

if 'PEBBLE_CONSUMER_KEY' in environ and 'PEBBLE_CONSUMER_SECRET' in environ:
    config['AUTH_PEBBLE'] = {
        'consumer_key': environ['PEBBLE_CONSUMER_KEY'],
        'consumer_secret': environ['PEBBLE_CONSUMER_SECRET']
    }
