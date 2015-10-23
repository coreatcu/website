PORT = 5000
DEBUG = True
HOST = '0.0.0.0'
DATA_FILENAMES = {
    'team': 'data/team.json',
    'initiatives': 'data/initiatives.json',
    'partners': 'data/partners.json'
}

SECRET_KEY = 'passwordgoeshere'
WTF_CSRF_ENABLED = True
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'coreatcu@gmail.com'
MAIL_PASSWORD = 'passwordgoeshere'
MAIL_DEFAULT_SENDER = 'coreboard@columbia.edu'