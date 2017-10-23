from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


class MyUserCreationForm(UserCreationForm):
    """
    Creates user without priveleges, with email address and password
    """
    error_messages = {
        'duplicate_email': 'Account with given email already exists.',
        'password_mismatch': 'Password mismatch.',
    }

    class Meta(UserCreationForm.Meta):
        model = User
        fields = '__all__'


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = '__all__'
