.. image:: https://travis-ci.org/vchaptsev/cookiecutter-django-vue.svg?branch=master
    :target: https://travis-ci.org/vchaptsev/cookiecutter-django-vue

Cookiecutter Django-Vue
=======================

Powered by Cookiecutter_, inspired by `Cookiecutter Django`_.

.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _`Cookiecutter Django`: https://github.com/pydanny/cookiecutter-django


.. image:: https://i.imgur.com/SA8cjs8.png
   :target: https://github.com/vchaptsev/cookiecutter-django-vue

Features
---------
* Docker_
* 12-Factor_
* Back: Django_
* Front: Vue.js_
* Server: Caddy_
* Database: PostgreSQL_
* Yarn_ for npm-dependencies
* Webpack_ for builds and hot-development-server
* Static & media files with AmazonS3_ or Whitenoise_
* Send emails via Anymail_ (using Mailgun_ by default)


Optional Integrations
---------------------

*These features can be enabled during initial project setup.*

* Integration with Travis_ for CI
* Integration with CKeditor_ for rich text editing
* Integration with MailHog_ for local email testing
* Integration with Sentry_ for frontend and backend errors logging
* Integration with `Google Analytics`_ or `Yandex Metrika`_ for web-analytics

.. _12-Factor: http://12factor.net/
.. _AmazonS3: https://aws.amazon.com/s3/
.. _Anymail: https://github.com/anymail/django-anymail
.. _Caddy: https://caddyserver.com/
.. _CKeditor: https://ckeditor.com/
.. _Django: https://www.djangoproject.com/
.. _Docker: https://www.docker.com/
.. _`Google Analytics`: https://www.google.com/analytics/
.. _LetsEncrypt: https://letsencrypt.org/
.. _Mailgun: http://www.mailgun.com/
.. _MailHog: https://github.com/mailhog/MailHog
.. _PostgreSQL: https://www.postgresql.org/
.. _Sentry: https://sentry.io/welcome/
.. _Travis: https://travis-ci.org/
.. _Vue.js: https://vuejs.org/
.. _Webpack: https://webpack.github.io/
.. _Whitenoise: http://whitenoise.evans.io/
.. _`Yandex Metrika`: https://tech.yandex.ru/metrika/
.. _Yarn: https://yarnpkg.com/


Usage
------

First, get Cookiecutter::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/vchaptsev/cookiecutter-django-vue

You'll be prompted for some values. Provide them, then a Django project will be created for you.

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
    ======================= DevOps ======================= [ ]:
    use_celery [y]: y
    use_travis [y]: y
    use_fabric_deployment [n]: n
    use_sentry [y]: y
    use_mailhog [y]: y
    Select static_and_media:
    1 - Amazon S3 (static and media)
    2 - Whitenoise (static) and Amazon S3 (media)
    3 - Whitenoise (static)
    Choose from 1, 2 [1]: 1
    ====================== FRONT-END ===================== [ ]:
    Select analytics:
    1 - Google Analytics
    2 - Yandex metrika
    3 - None
    Choose from 1, 2, 3 [1]: 1
    use_ckeditor [n]: n
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
