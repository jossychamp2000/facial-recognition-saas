'''Use this for production'''

from .base import *

DEBUG = False
ALLOWED_HOSTS += ['138.197.134.237']
WSGI_APPLICATION = 'home.wsgi.prod.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'facereconitionsaas',
        'USER': 'jossychamp2000',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

STRIPE_PUBLISH_KEY = 'pk_test_51GvuhsG2pgXqIT36lRYvFTt6qFMoO6pnEoAZSTBm00EQ7HDEx1FbIEPf0pqF6bAULYWdJupKNZt8yIvuVpn5Odhw00x8jbEP'
STRIPE_SECRET_KEY = 'sk_test_51GvuhsG2pgXqIT36FbQC0O7yRUtiAAAlGaSwVZizYhI4wp7cv0J1V16my336QYXOKr4cU16a9mlhbazidAEkpKIp0002LYNeTb'

CORS_ORIGIN_ALLOW_ALL = True
