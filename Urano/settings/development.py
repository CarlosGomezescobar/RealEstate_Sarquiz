from .base import *



DEFAULT_FROM_EMAIL = "info@urano_realestate.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Urano Real Estate"



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}

