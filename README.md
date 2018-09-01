Cookiecutter Django-Vue
=======================

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter),
inspired by [Cookiecutter Django](https://github.com/pydanny/cookiecutter-django).

<p align="center">
  <img src="https://i.imgur.com/SA8cjs8.png" />
</p>


Features
--------

-   [Docker](https://www.docker.com/)
-   [12 Factor](http://12factor.net/)
<!-- -   Server: [Caddy](https://caddyserver.com/) -->
-   Frontend: [Vue](https://vuejs.org/) + vue-cli
-   Backend: [Django](https://www.djangoproject.com/)
-   Database: [PostgreSQL](https://www.postgresql.org/)
<!-- -   [pipenv](https://github.com/pypa/pipenv) for python-requirements -->
-   Send emails via [Anymail](https://github.com/anymail/django-anymail)
    (using [Mailgun](http://www.mailgun.com/) by default)

Optional Integrations
---------------------

*These features can be enabled during initial project setup.*

-   Integration with [MailHog](https://github.com/mailhog/MailHog) for local email testing
-   Integration with [Sentry](https://sentry.io/welcome/) for frontend and backend errors logging
-   Integration with [Google Analytics](https://www.google.com/analytics/) or [Yandex Metrika](https://tech.yandex.ru/metrika/) for web-analytics

Usage
-----

First, get `cookiecutter`:

    $ pip install cookiecutter

Now run it against this repo:

    $ cookiecutter gh:vchaptsev/cookiecutter-django-vue

You'll be prompted for some values. Provide them, then a  project
will be created for you.

Answer the prompts with your own desired options. For example:

    ======================= GENERAL ====================== [ ]:
    project_name [Project Name]: Website
    project_slug [website]: website
    description [Short description]: My awesome website
    author [Your Name]: Your Name
    email [<admin@website.com>]: <admin@website.com>
    ======================= DEVOPS ======================= [ ]:
    use_sentry [y]: y
    ======================= BACKEND ====================== [ ]:
    use_mailhog [y]: y
    custom_user [n]: n
    ======================= FRONTEND ===================== [ ]:
    Select analytics:
    1 - Google Analytics
    2 - Yandex Metrika
    3 - None
    Choose from 1, 2, 3 [1]: 2

Now you can start project with
[docker-compose](https://docs.docker.com/compose/):

    $ docker-compose up --build

For production you'll need to fill out `.env` file and use
`docker-compose-prod.yml` file:

    $ docker-compose -f docker-compose-prod.yml up --build -d
