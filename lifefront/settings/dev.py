from .common import *

DEBUG = False

SECRET_KEY = 'django-insecure--($@v)az%#d$ktpsze@1_jj_5_@zr)sw%)ws^1vh_q+(p)n2ma'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}