'''Use this for development'''

from .base import *

ALLOWED_HOSTS += ['127.0.0.1']
DEBUG = True

WSGI_APPLICATION = 'home.wsgi.dev.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
)

STRIPE_PUBLISH_KEY = 'pk_test_51GvuhsG2pgXqIT36lRYvFTt6qFMoO6pnEoAZSTBm00EQ7HDEx1FbIEPf0pqF6bAULYWdJupKNZt8yIvuVpn5Odhw00x8jbEPmC'
STRIPE_SECRET_KEY = 'sk_test_51GvuhsG2pgXqIT36FbQC0O7yRUtiAAAlGaSwVZizYhI4wp7cv0J1V16my336QYXOKr4cU16a9mlhbazidAEkpKIp0002LYNeTb'
