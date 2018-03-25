#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

python /app/manage.py migrate
python /app/manage.py collectstatic --noinput --verbosity 0
/usr/local/bin/gunicorn config.wsgi -w 4 --worker-class gevent -b 0.0.0.0:5000 --chdir=/app
