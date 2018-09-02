#!/bin/sh

# install test requirements
pip install -r requirements.txt

# create a cache directory
mkdir -p .cache/docker && cd .cache/docker

#======================================================================
# DEFAULT SETTINGS
cookiecutter ../../ --no-input --overwrite-if-exists && cd project_name

docker-compose run backend python manage.py check
