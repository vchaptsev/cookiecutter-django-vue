import factory
from uuid import uuid4


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Sequence(lambda n: f'user-{n}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'password')
    first_name = 'First'
    last_name = 'Last'
    token = uuid4()

    class Meta:
        model = 'users.User'
        django_get_or_create = ['email']
