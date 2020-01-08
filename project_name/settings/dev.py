from .common import *

DEBUG = True

WSGI_APPLICATION = '%s.wsgi.dev.application'

ALLOWED_HOSTS += ['*']

SECRET_FILE = os.path.join(BASE_DIR, 'dev', 'django_key.txt')

# uncomment the following line to include i18n
# from .i18n import *

try:
    SECRET_KEY = open(SECRET_FILE).read().strip()
except IOError:
    try:
        import random

        SECRET_KEY = ''.join(
            [random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
        secret = open(SECRET_FILE, 'w')
        secret.write(SECRET_KEY)
        secret.close()
    except IOError:
        Exception('Please create a %s file with random characters \
        to generate your secret key!' % SECRET_FILE)

# create dir
database_path = os.path.join(BASE_DIR, 'dev')
if not os.path.isdir(database_path):
    os.mkdir(database_path)

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(database_path, 'db.sqlite3'),
    }
}

# EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
