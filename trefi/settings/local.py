import os
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l+7seat+x)aoeg1bm_8@$4&9!gm08qn%*rf4@1mdm7c6l@$8%('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Trefi_db',
        'USER': 'Trefi_admin',
        'PASSWORD': 'Trefi1209',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


STATICFILES_DIRS = [os.path.join(os.getcwd(), 'static')]