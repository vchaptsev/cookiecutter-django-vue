from uuid import uuid4

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        user = self.model(email=self.normalize_email(email),
                          is_active=True,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          last_login=timezone.now(),
                          registered_at=timezone.now(),
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create(self, **extra_fields):
        email = extra_fields.pop('email')
        password = extra_fields.pop('password', '')
        return self.create_user(email, password, **extra_fields)

    def create_user(self, email=None, password=None, **extra_fields):
        is_staff = extra_fields.pop('is_staff', False)
        is_superuser = extra_fields.pop('is_superuser', False)
        return self._create_user(email, password, is_staff, is_superuser, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, is_staff=True, is_superuser=True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=_('Email'), unique=True, max_length=255)
    first_name = models.CharField(verbose_name=_('First name'), max_length=30, blank=True)
    last_name = models.CharField(verbose_name=_('Last name'), max_length=30, blank=True)
    middle_name = models.CharField(verbose_name=_('Middle name'), max_length=30, blank=True)

    avatar = models.ImageField(verbose_name=_('Avatar'), blank=True)
    phone = models.CharField(verbose_name=_('Phone'), max_length=30, blank=True)
    position = models.CharField(verbose_name=_('Position'), max_length=150, blank=True)
    address = models.CharField(verbose_name=_('Address'), max_length=300, blank=True)
    token = models.UUIDField(verbose_name=_('Token'), default=uuid4, editable=False)

    is_admin = models.BooleanField(verbose_name=_('Admin'), default=False)
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    is_staff = models.BooleanField(verbose_name=_('Staff'), default=False)

    registered_at = models.DateTimeField(verbose_name=_('Registered at'), auto_now_add=timezone.now)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    full_name.fget.short_description = _('Full name')

    @property
    def short_name(self):
        last_name = self.last_name
        first_name = self.first_name[0] + '.' if self.first_name else ''
        middle_name = self.middle_name[0] + '.' if self.middle_name else ''

        return f'{last_name} {first_name}{middle_name}'

    def get_short_name(self):
        return self.short_name

    def get_full_name(self):
        return self.full_name

    def __str__(self):
        return self.full_name
