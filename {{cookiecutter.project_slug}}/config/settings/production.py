"""
Production Configurations

- Use mailgun to send emails
- Use Redis for cache
{% if cookiecutter.use_sentry == 'y' -%}
- Use Sentry for error logging
{% endif %}
{% if cookiecutter.static_and_media == 'Amazon S3 (static and media)' -%}
- Use Amazon S3 files
{% elif cookiecutter.static_and_media == 'Whitenoise (static) and Amazon S3 (media)' %}
- Use Whitenoise for static and Amazon S3 for media
{% else %}
- Use Whitenoise for static
{% endif %}
"""

import logging
from datetime import datetime, timedelta

from .base import *  # noqa

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Raises ImproperlyConfigured exception if DJANGO_SECRET_KEY not in os.environ
SECRET_KEY = env('DJANGO_SECRET_KEY')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

{% if cookiecutter.static_and_media != 'Amazon S3 (static and media)' -%}
# Use Whitenoise to serve static files
# See: https://whitenoise.readthedocs.io/
WHITENOISE_MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware']
MIDDLEWARE = WHITENOISE_MIDDLEWARE + MIDDLEWARE
{% endif %}

{% if cookiecutter.use_sentry == 'y' -%}
# raven sentry client
# See https://docs.sentry.io/clients/python/integrations/django/
INSTALLED_APPS += ['raven.contrib.django.raven_compat']
RAVEN_MIDDLEWARE = ['raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware']
MIDDLEWARE = RAVEN_MIDDLEWARE + MIDDLEWARE
{% endif %}


# SITE CONFIGURATION
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=[''])
DOMAIN = env('DJANGO_DOMAIN', default='{{cookiecutter.domain}}')

# Gunicorn
INSTALLED_APPS += ['gunicorn']


# STORAGE CONFIGURATION
# ------------------------------------------------------------------------------
# Uploaded Media Files
# ------------------------
# See: http://django-storages.readthedocs.io/en/latest/index.html
INSTALLED_APPS += ['storages']

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_STORAGE_BUCKET_REGION = env('AWS_STORAGE_BUCKET_REGION')
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False
AWS_IS_GZIPPED = True

# AWS cache settings
AWS_EXPIRY = timedelta(days=30).total_seconds()

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': (datetime.now() + timedelta(days=30)).strftime('%a, %d %b %Y 00:00:00 GMT'),
    'CacheControl': 'max-age=%d, s-maxage=%d, must-revalidate'.format(AWS_EXPIRY, AWS_EXPIRY)
}

{% if cookiecutter.static_and_media == 'Amazon S3 (static and media)' -%}
from storages.backends.s3boto3 import S3Boto3Storage
StaticRootS3BotoStorage = lambda: S3Boto3Storage(location='static')
MediaRootS3BotoStorage = lambda: S3Boto3Storage(location='media')
DEFAULT_FILE_STORAGE = 'config.settings.production.MediaRootS3BotoStorage'
MEDIA_URL = 'https://{}.s3.{}.amazonaws.com/media/'.format(AWS_STORAGE_BUCKET_NAME, AWS_STORAGE_BUCKET_REGION)

# Static Assets
# ------------------------
STATIC_URL = 'https://{}.s3.{}.amazonaws.com/static/'.format(AWS_STORAGE_BUCKET_NAME, AWS_STORAGE_BUCKET_REGION)
STATICFILES_STORAGE = 'config.settings.production.StaticRootS3BotoStorage'
AWS_PRELOAD_METADATA = True
INSTALLED_APPS = ['collectfast'] + INSTALLED_APPS
{% elif cookiecutter.static_and_media == 'Whitenoise (static) and Amazon S3 (media)' %}
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = 'https://{}.s3.{}.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME, AWS_STORAGE_BUCKET_REGION)
{%- endif %}

# EMAIL
# ------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL', default='{{cookiecutter.project_name}} <noreply@{{cookiecutter.domain}}>')
EMAIL_SUBJECT_PREFIX = env('DJANGO_EMAIL_SUBJECT_PREFIX', default='[{{cookiecutter.project_name}}]')
SERVER_EMAIL = env('DJANGO_SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)

# Anymail with Mailgun
INSTALLED_APPS += ['anymail']
ANYMAIL = {
    'MAILGUN_API_KEY': env('DJANGO_MAILGUN_API_KEY'),
    'MAILGUN_SENDER_DOMAIN': env('MAILGUN_SENDER_DOMAIN')
}
EMAIL_BACKEND = 'anymail.backends.mailgun.MailgunBackend'

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See:
# https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.cached.Loader
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader', 'django.template.loaders.app_directories.Loader', ]),
]

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------

# Use the Heroku-style specification
# Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
DATABASES['default'] = env.db('DATABASE_URL')

# CACHING
# ------------------------------------------------------------------------------

REDIS_LOCATION = '{0}/{1}'.format(env('REDIS_URL', default='redis://127.0.0.1:6379'), 0)
# Heroku URL does not pass the DB number, so we parse it in
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_LOCATION,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True,  # mimics memcache behavior.
                                        # http://niwinz.github.io/django-redis/latest/#_memcached_exceptions_behavior
        }
    }
}

{% if cookiecutter.use_sentry == 'y' -%}
# Sentry Configuration
SENTRY_DSN = env('DJANGO_SENTRY_DSN')
SENTRY_CLIENT = env('DJANGO_SENTRY_CLIENT', default='raven.contrib.django.raven_compat.DjangoClient')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry', ],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console', ],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console', ],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console', ],
            'propagate': False,
        },
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['console', 'sentry', ],
            'propagate': False,
        },
    },
}

SENTRY_CELERY_LOGLEVEL = env.int('DJANGO_SENTRY_LOG_LEVEL', logging.INFO)
RAVEN_CONFIG = {
    'CELERY_LOGLEVEL': env.int('DJANGO_SENTRY_LOG_LEVEL', logging.INFO),
    'DSN': SENTRY_DSN
}
{% endif %}
