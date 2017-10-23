"""
Local settings

- Run in Debug mode
{% if cookiecutter.use_mailhog == 'y' -%}
- Use mailhog for emails
{% endif %}
- Add django-extensions as app
"""

from .base import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY', default='d+fr=mPvpaeaK)^Emob/<Sf4?[L}?_T&B&i5(MxL.i5O[D_b!^')

# Mail settings
# ------------------------------------------------------------------------------

EMAIL_PORT = 1025
{% if cookiecutter.use_mailhog == 'y' -%}
EMAIL_HOST = env('EMAIL_HOST', default='mailhog')
{% endif %}

# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
