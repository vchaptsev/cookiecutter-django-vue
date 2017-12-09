#!/bin/sh

# install test requirements
pip install -r requirements.txt

# create a cache directory
mkdir -p .cache/docker && cd .cache/docker

#======================================================================
# DEFAULT SETTINGS
cookiecutter ../../ --no-input --overwrite-if-exists && cd project_name

# run the project's tests
docker-compose run django py.test
