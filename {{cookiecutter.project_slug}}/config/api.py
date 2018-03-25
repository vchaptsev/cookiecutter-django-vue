from rest_framework import routers
{% if cookiecutter.custom_user == 'y' %}
from {{cookiecutter.project_slug}}.users.views import UserViewSet
{% endif %}

# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

{% if cookiecutter.custom_user == 'y' %}
# Users API
api.register(r'users', UserViewSet)
{% endif %}
