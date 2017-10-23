import factory
from uuid import uuid4


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Sequence(lambda n: 'user-{0}@example.com'.format(n))
    password = factory.PostGenerationMethodCall('set_password', 'password')
    first_name = 'First'
    middle_name = 'Middle'
    last_name = 'Last'
    token = uuid4()

    class Meta:
        model = 'users.User'
        django_get_or_create = ['email']
