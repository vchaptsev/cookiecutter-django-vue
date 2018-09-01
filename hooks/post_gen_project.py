"""
1. Generates and saves random secret key
2. Renames env.example to .env
3. Removes users app if it isn't going to be used
"""
import os
import random
import string
import shutil

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def set_secret_key(file_location):
    """ Generates and saves random secret key """
    with open(file_location) as f:
        file_ = f.read()

    punctuation = string.punctuation.replace('"', '').replace("'", '').replace('\\', '')
    secret = ''.join(random.choice(string.digits + string.ascii_letters + punctuation) for i in range(50))
    file_ = file_.replace('CHANGEME!!!', secret, 1)

    # Write the results
    with open(file_location, 'w') as f:
        f.write(file_)


def rename_env_file():
    """ Renames env file """
    os.rename(os.path.join(PROJECT_DIRECTORY, 'env.example'), os.path.join(PROJECT_DIRECTORY, '.env'))

def remove_users_app():
    """ Removes users app if it isn't going to be used """
    users_app = os.path.join(PROJECT_DIRECTORY, '{{ cookiecutter.project_slug }}/users')
    shutil.rmtree(users_app)

    for filename in ['modules/auth.js', 'services/users.js']:
        os.remove(os.path.join(PROJECT_DIRECTORY, '{{ cookiecutter.project_slug }}/static/store/' + filename))

# Removes users app if it isn't going to be used
if '{{ cookiecutter.custom_user }}' == 'n':
    remove_users_app()

# Generates and saves random secret key
set_secret_key(os.path.join(PROJECT_DIRECTORY, 'env.example'))  # env file

# Renames env file
rename_env_file()
