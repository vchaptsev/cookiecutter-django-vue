from test_plus.test import TestCase

from ..models import User
from .factories import UserFactory


class TestUser(TestCase):
    user_factory = UserFactory

    def setUp(self):
        self.user = self.make_user()

    def test_full_name(self):
        self.assertEqual(self.user.get_full_name(), 'First Last')

    def test_short_name(self):
        self.assertEqual(self.user.get_short_name(), 'Last F.')

    def test_string_representation(self):
        self.assertEqual(str(self.user), 'First Last')

    def test_create(self):
        extra_fields = {'email': 'test@email.com', 'password': 'password', 'first_name': 'test'}
        user = User.objects.create(**extra_fields)
        self.assertEqual(user.email, 'test@email.com')
        self.assertEqual(user.first_name, 'test')

    def test_create_user(self):
        user = User.objects.create_user(email='user@email.com', password='password')
        self.assertEqual(user.email, 'user@email.com')

    def test_create_superuser(self):
        user = User.objects.create_superuser(email='user@email.com', password='password')
        self.assertEqual(user.email, 'user@email.com')
