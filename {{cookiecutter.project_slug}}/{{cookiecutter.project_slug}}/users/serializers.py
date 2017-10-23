from rest_framework import serializers
from django.conf import settings

from .models import User


class UserSerializer(serializers.ModelSerializer):
    registered_at = serializers.DateTimeField(format='%H:%M %d.%m.%Y', read_only=True)

    avatar_url = serializers.SerializerMethodField(read_only=True)
    short_name = serializers.SerializerMethodField(read_only=True)
    full_name = serializers.SerializerMethodField(read_only=True)

    def get_avatar_url(self, obj):
        return obj.avatar.url if obj.avatar else settings.STATIC_URL + 'images/default_avatar.png'

    def get_short_name(self, obj):
        return obj.short_name

    def get_full_name(self, obj):
        return obj.full_name

    class Meta:
        model = User
        exclude = ['password', 'is_staff', 'is_active',
                   'groups', 'user_permissions', 'first_name',
                   'last_name', 'middle_name']


class UserWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['is_active']
