from .base import *
from base import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['programmer-plebeian.herokuapp.com']


# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
#this is a test comment
