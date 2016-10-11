PORT = 5000
DEBUG = True
HOST = '0.0.0.0'
DATA_FILENAMES = {
    'team': 'data/team.json',
    'alumni': 'data/alumni.json',
    'initiatives': 'data/initiatives.json',
    'partners': 'data/partners.json'
}

SECRET_KEY = 'secret key goes here'
WTF_CSRF_ENABLED = True
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'coreatcu@gmail.com'
MAIL_PASSWORD = 'passwordgoeshere'
MAIL_DEFAULT_SENDER = 'coreboard@columbia.edu'
RECAPTCHA_PUBLIC_KEY = '6Lf65CYTAAAAAOfIyFm4K07j_ugoP_iMPNGD-tIl'
RECAPTCHA_PRIVATE_KEY = '6Lf65CYTAAAAAMN4BaWRqaECoQEKtA6v3ZylcVpm'
