from .base import *
  
#DEBUG = False

CSRF_TRUSTED_ORIGINS = ['https://*.carlhub.com','https://*.127.0.0.1']

INTERNAL_IPS = ['127.0.0.1',]

ALLOWED_HOSTS = ['carlhub.com','localhost']
SECRET_KEY = os.environ['SECRET_KEY']

SITE_ID = 1
MEDIA_ROOT = "/home/xorb/media"
STATIC_ROOT = "/home/xorb/static"

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': '127.0.0.1',
        'PORT':'5432',
     }
}


