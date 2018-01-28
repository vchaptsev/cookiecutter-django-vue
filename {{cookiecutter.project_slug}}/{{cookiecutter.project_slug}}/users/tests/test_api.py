from uuid import uuid4

from test_plus.test import TestCase

from ..models import User
from .factories import UserFactory


class UserTests(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.another_user = UserFactory()

    def test_profile(self):
        # wihout login
        response = self.get('user-profile')
        self.response_401(response)

        # with login
        with self.login(username=self.user.email):
            response = self.get('user-profile')
            self.response_200(response)

    def test_login(self):
        # success
        data = {'email': self.user.email, 'password': 'password'}
        response = self.post('user-login', data=data)
        self.response_200(response)

        # fail
        data = {'email': self.user.email, 'password': 'bad_password'}
        response = self.post('user-login', data=data)
        self.response_404(response)

    def test_list(self):
        with self.login(username=self.user.email):
            response = self.get('user-list')
            self.response_200(response)
            self.assertEqual(len(response.json()), 2)

    def test_detail(self):
        with self.login(username=self.user.email):
            response = self.get('user-detail', pk=self.user.id)
            self.response_200(response)

    def test_delete(self):
        with self.login(username=self.user.email):
            response = self.delete('user-detail', pk=self.user.id)
            self.assertEqual(response.status_code, 204)

    def test_update(self):
        with self.login(username=self.user.email):
            response = self.get('user-detail', pk=self.user.id, data={'password': 'new_password'})
            self.response_200(response)
            self.assertEqual(self.user.password == User.objects.last().password, False)

    def test_create(self):
        with self.login(username=self.user.email):
            data = {
                'email': 'test_create@gmail.com',
                'password': 'password',
                'first_name': 'first_name',
                'last_name': 'last_name'
            }
            response = self.post('user-list', data=data)
            self.response_201(response)
            self.assertEqual(response.json()['email'], 'test_create@gmail.com')

    def test_register(self):
        with self.login(username=self.user.email):
            UserFactory(email='test_reg@gmail.com')

            # user with email already exists
            data = {
                'email': 'test_reg@gmail.com',
                'password': 'password',
                'first_name': 'first',
                'last_name': 'last',
                'avatar': ''
            }
            response = self.post('user-register', data=data)
            self.response_200(response)
            self.assertEqual(response.json()['status'], 210)

            # successful registration
            data = {
                'email': 'test_reg_new@gmail.com',
                'password': 'password',
                'first_name': 'first',
                'last_name': 'last',
                'avatar': ''
            }
            response = self.post('user-register', data=data)
            self.response_201(response)

    def test_password_reset(self):
        with self.login(username=self.user.email):
            # successful password reset
            response = self.post('user-password-reset', data={'email': self.user.email})
            self.response_200(response)

            # email doesn't exist
            response = self.post('user-password-reset', data={'email': 'fake-email@gmail.com'})
            self.response_404(response)

    def test_password_change(self):
        with self.login(username=self.user.email):
            current_password = self.user.password

            # token doesn't exist
            response = self.post('user-password-change', data={'token': uuid4(), 'password': 'new_password'})
            self.response_404(response)
            self.assertEqual(current_password, self.user.password)

            # successful password change
            self.user.token = uuid4()
            self.user.save()
            response = self.post('user-password-change', data={'token': self.user.token, 'password': 'new_password'})
            self.response_200(response)
            self.assertEqual(current_password == User.objects.last().password, False)
