from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UsersConfig(AppConfig):
    name = '{{cookiecutter.project_slug}}.users'
    verbose_name = _('Users')
