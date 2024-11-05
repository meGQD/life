import os
from .common import *

DEBUG = False

SECRET_KEY = os.getenv("SECRET_KEY")
print(f"Loaded SECRET_KEY: {SECRET_KEY}")


ALLOWED_HOSTS = ["localhost", "0.0.0.0", "https://elastic-aryabhata-qzkaaw7ph.liara.run/", "elastic-aryabhata-qzkaaw7ph.liara.run/"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}