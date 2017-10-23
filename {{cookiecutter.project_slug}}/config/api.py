from rest_framework import routers

from {{cookiecutter.project_slug}}.users.views import UserViewSet

# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

# Users API
api.register(r'users', UserViewSet)
