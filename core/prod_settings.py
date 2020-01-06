from core import settings
import os

DEBUG = False
ALLOWED_HOSTS = []

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '8on$iujotn1zl^5t1+_elot62^y(wl4-7i-zu=*050x+q3l32p')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '../my.cnf',
        },
    }
}
