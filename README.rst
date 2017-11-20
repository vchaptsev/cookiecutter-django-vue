Cookiecutter Django-Vue
=======================

Powered by Cookiecutter_, inspired by `Cookiecutter Django`_.

.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _`Cookiecutter Django`: https://github.com/pydanny/cookiecutter-django


.. image:: https://i.imgur.com/SA8cjs8.png
   :name: cookiecutter-django-vue
   :align: center
   :alt: cookiecutter-django-vue
   :target: https://github.com/vchaptsev/cookiecutter-django-vue

Features
---------

* Docker_-based
* For Django_ 1.11
* Vue_ framework
* Works with Python 3.6
* PostgreSQL_ database
* Caddy_ server with LetsEncrypt_ integration

* Optimized development and production settings (12-Factor_ based via django-environ_)
* Send emails via Anymail_ (using Mailgun_ by default, but switchable)
* Static & media files with AmazonS3 or Whitenoise_ + AmazonS3
* Webpack_ for builds and hot-development-server
* Yarn_ for npm-dependencies

Optional Integrations
---------------------

*These features can be enabled during initial project setup.*

* Integration with Travis_ for CI
* Integration with Sentry_ for error logging
* Integration with MailHog_ for local email testing
* Integration with `Google Analytics` or `Yandex Metrika`_ for web-analytics
* Integration with CKeditor_ for rich text editing

.. _Django: https://www.djangoproject.com/
.. _django-environ: https://github.com/joke2k/django-environ
.. _12-Factor: http://12factor.net/
.. _Mailgun: http://www.mailgun.com/
.. _Anymail: https://github.com/anymail/django-anymail
.. _MailHog: https://github.com/mailhog/MailHog
.. _Sentry: https://sentry.io/welcome/
.. _Caddy: https://caddyserver.com/
.. _LetsEncrypt: https://letsencrypt.org/
.. _Webpack: https://webpack.github.io/
.. _Yarn: https://yarnpkg.com/
.. _Vue: https://vuejs.org/
.. _Travis: https://travis-ci.org/
.. _`Google Analytics`: https://www.google.com/analytics/
.. _`Yandex Metrika`: https://tech.yandex.ru/metrika/
.. _CKeditor: https://ckeditor.com/
.. _Docker: https://www.docker.com/
.. _PostgreSQL: https://www.postgresql.org/
.. _Whitenoise: http://whitenoise.evans.io/

Usage
------

Let's pretend you want to create a Django project called "my_awesome_website". Rather than using `startproject`
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter_ to do all the work.

First, get Cookiecutter. Trust me, it's awesome::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/vchaptsev/cookiecutter-django-vue

You'll be prompted for some values. Provide them, then a Django project will be created for you.

**Warning**: After this point, change 'Daniel Greenfeld', etc to your own information.

Answer the prompts with your own desired options. For example::

    ======================= GENERAL ====================== [ ]:
    project_name [Project Name]: Website
    project_slug [website]: website
    domain [website.com]: website.com
    description [A short description of the project.]: My awesome website
    author [Daniel Roy Greenfeld]: Your Name
    email [admin@website.com]: admin@website.com
    version [0.1]: 0.1
    Select license:
    1 - MIT
    2 - BSD
    3 - GPLv3
    4 - Apache Software License 2.0
    5 - Not open source
    Choose from 1, 2, 3, 4, 5 [1]: 1
    Select use_ckeditor:
    1 - Everywhere
    2 - Backend
    3 - Frontend
    4 - Don't use
    ======================= DevOps ======================= [ ]:
    use_celery [y]: y
    use_travis [y]: y
    use_sentry [y]: y
    use_mailhog [y]: y
    Select static_and_media:
    1 - Amazon S3 for static and media
    2 - Whitenoise for static, Amazon S3 for media
    Choose from 1, 2 [1]: 1
    ====================== FRONT-END ===================== [ ]:
    Select analytics:
    1 - Google Analytics
    2 - Yandex metrika
    3 - None
    use_progressbar [n]: n
    use_vue_material [n]: n

Now you can start project with `docker-compose`_::

    $ docker-compose up --build

For production you'll need to fill out .env file and use docker-compose-prod.yml file::

    $ docker-compose -f docker-compose-prod.yml up --build -d


If you want to use travis + fabric ssh deployment, you'll need to set up PRODUCTION_USER and PRODUCTION_PASSWORD `encrypted envs`_ to .travis.yml::

    $ travis encrypt PRODUCTION_USER=user --add env.global
    $ travis encrypt PRODUCTION_PASSWORD=secret --add env.global


.. _`encrypted envs`: https://docs.travis-ci.com/user/environment-variables/#Encrypting-environment-variables
.. _`docker-compose`: https://docs.docker.com/compose/
