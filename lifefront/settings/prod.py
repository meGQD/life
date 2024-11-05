import os
from .common import *

DEBUG = False

SECRET_KEY = 'fd9+if!o&4mdn5dixonjirs%t4453h_&%a26=t0j*v1sm_+2k_'

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "https://elastic-aryabhata-qzkaaw7ph.liara.run/", "elastic-aryabhata-qzkaaw7ph.liara.run/"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}