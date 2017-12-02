import pytest


@pytest.fixture
def context():
    return {
        'project_name': 'test',
        'project_slug': 'test',
        'domain': 'test.com',
        'description': 'A short description of the project.',
        'author': 'author',
        'email': 'author@test.com',
        'version': '0.1.0'
    }


def test_default(cookies, context):
    """
    Test default config
    """
    result = cookies.bake(extra_context=context)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.isdir()
    assert result.project.basename == context['project_slug']
