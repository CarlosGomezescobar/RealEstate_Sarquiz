from .base import *

# DATABASES = {
#     "default": {
#         "ENGINE":env("POSTGRES_ENGINE"),
#         "NAME": env("POSTGRES_DB"),
#         "USER": env("POSTGRES_USER"),
#         "PASSWORD": env("POSTGRES_PASSWORD"),
#         "HOST": env("PG_HOST"),
#         "PORT": env("PG_PORT"),

#     }
# }

# EMAiL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = env("EMAIL_HOST")
# EMAIL_USE_TLS = True
# EMAIL_PORT = env("EMAIL_PORT")
# EMAIL_HOST_USER = env("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
# DEFAULT_FROM_EMAIL = "info@urano_realestate.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Urano Real Estate"



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}