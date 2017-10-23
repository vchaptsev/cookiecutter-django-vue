#!/bin/sh
python manage.py migrate
/usr/local/bin/gunicorn config.wsgi -w 4 --worker-class gevent -b 0.0.0.0:5000 --chdir=/app
