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

{% comment %} AWS_STORAGE_BUCKET_NAME=os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_REGION_NAME=os.environ['AWS_S3_REGION_NAME']
AWS_ACCESS_KEY_ID=os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRE_ACCESST_KEY=os.environ['AWS_SECRET_ACCESS_KEY'] {% endcomment %}

