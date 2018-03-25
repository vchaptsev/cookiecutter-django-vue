'''
1. Generates and saves random secret key
2. Renames env.example to .env
3. Removes .travis.yml if travis isn't going to be used
4. Removes files conventional to opensource projects only
5. Removes users app if it isn't going to be used
'''
import os
import random
import string
import shutil

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_copying_files():
    '''
    Removes files needed for the GPLv3 licence if it isn't going to be used
    '''
    for filename in ['COPYING']:
        os.remove(os.path.join(PROJECT_DIRECTORY, filename))


def remove_open_source_files():
    '''
    Removes files conventional to opensource projects only.
    '''
    for filename in ['CONTRIBUTORS.txt']:
        os.remove(os.path.join(PROJECT_DIRECTORY, filename))


def set_secret_key(file_location):
    '''
    Generates and saves random secret key
    '''
    with open(file_location) as f:
        file_ = f.read()

    punctuation = string.punctuation.replace('"', '').replace("'", '').replace('\\', '')
    secret = ''.join(random.choice(string.digits + string.ascii_letters + punctuation) for i in range(50))
    file_ = file_.replace('CHANGEME!!!', secret, 1)

    # Write the results
    with open(file_location, 'w') as f:
        f.write(file_)


def rename_env_file():
    '''
    Renames env file
    '''
    os.rename(os.path.join(PROJECT_DIRECTORY, 'env.example'), os.path.join(PROJECT_DIRECTORY, '.env'))


def remove_travis_file():
    '''
    Removes travis file if it isn't going to be used
    '''
    for filename in ['.travis.yml']:
        os.remove(os.path.join(PROJECT_DIRECTORY, filename))


def remove_users_app():
    '''
    Removes users app if it isn't going to be used
    '''
    users_app = os.path.join(PROJECT_DIRECTORY, '{{ cookiecutter.project_slug }}/users')
    shutil.rmtree(users_app)

    for filename in ['modules/auth.js', 'services/users.js']:
        os.remove(os.path.join(PROJECT_DIRECTORY, '{{ cookiecutter.project_slug }}/static/'))


# Removes files needed for the GPLv3 licence if it isn't going to be used.
if '{{ cookiecutter.license}}' != 'GPLv3':
    remove_copying_files()

# Remove files conventional to opensource projects only.
if '{{ cookiecutter.license }}' == 'Not open source':
    remove_open_source_files()

# Removes travis file if it isn't going to be used
if '{{ cookiecutter.use_travis }}' == 'n':
    remove_travis_file()

# Removes users app if it isn't going to be used
if '{{ cookiecutter.custom_user }}' == 'n':
    remove_users_app()

# Generates and saves random secret key
set_secret_key(os.path.join(PROJECT_DIRECTORY, 'env.example'))  # env file
set_secret_key(os.path.join(PROJECT_DIRECTORY, 'config/settings/local.py'))  # local settings

# Renames env file
rename_env_file()
