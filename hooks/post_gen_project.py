"""
1. Generates and saves random secret key
2. Renames env.example to .env
3. Removes the taskapp if celery isn't going to be used
4. Removes .travis.yml if travis isn't going to be used
5. Removes fabfile.py if ssh_deployment isn't going to be used
6. Removes files conventional to opensource projects only
"""
import os
import random
import shutil
import string

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_copying_files():
    """
    Removes files needed for the GPLv3 licence if it isn't going to be used
    """
    for filename in ["COPYING"]:
        os.remove(os.path.join(PROJECT_DIRECTORY, filename))


def remove_open_source_files():
    """
    Removes files conventional to opensource projects only.
    """
    for filename in ["CONTRIBUTORS.txt"]:
        os.remove(os.path.join(PROJECT_DIRECTORY, filename))


def set_secret_key(file_location):
    """Generates and saves random secret key"""
    with open(file_location) as f:
        file_ = f.read()

    punctuation = string.punctuation.replace('"', '').replace("'", '').replace('\\', '')
    secret = ''.join(random.choice(string.digits + string.ascii_letters + punctuation) for i in range(50))
    file_ = file_.replace('CHANGEME!!!', secret, 1)

    # Write the results
    with open(file_location, 'w') as f:
        f.write(file_)


def rename_env_file():
    """Renames env file"""
    os.rename(os.path.join(PROJECT_DIRECTORY, 'env.example'), os.path.join(PROJECT_DIRECTORY, '.env'))


def remove_task_app():
    """Removes celery files if celery isn't going to be used"""
    task_app = os.path.join(PROJECT_DIRECTORY, '{{ cookiecutter.project_slug }}/taskapp')
    shutil.rmtree(task_app)

    celery_local = os.path.join(PROJECT_DIRECTORY, 'compose/local/django/celery')
    shutil.rmtree(celery_local)

    celery_prod = os.path.join(PROJECT_DIRECTORY, 'compose/production/django/celery')
    shutil.rmtree(celery_prod)


def remove_travis_file():
    """
    Removes travis file if it isn't going to be used
    """
    for filename in [".travis.yml"]:
        os.remove(os.path.join(PROJECT_DIRECTORY, filename))


def remove_fabric_file():
    """
    Removes fabric file if it isn't going to be used
    """
    for filename in ["fabfile.py"]:
        os.remove(os.path.join(PROJECT_DIRECTORY, filename))


# Removes files needed for the GPLv3 licence if it isn't going to be used.
if '{{ cookiecutter.license}}' != 'GPLv3':
    remove_copying_files()

# Remove files conventional to opensource projects only.
if '{{ cookiecutter.license }}' == 'Not open source':
    remove_open_source_files()

# Removes the taskapp if celery isn't going to be used
if '{{ cookiecutter.use_celery }}'.lower() == 'n':
    remove_task_app()

# Removes travis file if it isn't going to be used
if '{{ cookiecutter.use_travis }}'.lower() == 'n':
    remove_travis_file()

# Removes fabric file if it isn't going to be used
if '{{ cookiecutter.use_fabric_deployment }}'.lower() == 'n':
    remove_fabric_file()

# Generates and saves random secret key
set_secret_key(os.path.join(PROJECT_DIRECTORY, 'env.example'))  # env file
set_secret_key(os.path.join(PROJECT_DIRECTORY, 'config/settings/local.py'))  # local settings

# Renames env file
rename_env_file()
