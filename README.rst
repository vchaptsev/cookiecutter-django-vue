Cookiecutter Django-Vue
=======================

Powered by Cookiecutter_, based on `Cookiecutter Django`_.
Dockerized.

.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _`Cookiecutter Django`: https://github.com/pydanny/cookiecutter-django

Features
---------

* Docker_-based
* For Django 1.11
* Works with Python 3.6
* 12-Factor_ based settings via django-environ_
* Optimized development and production settings
* Comes with custom user model ready to go
* Send emails via Anymail_ (using Mailgun_ by default, but switchable)
* Static & media storages using Amazon S3
* Run tests with py.test
* Webpack_ for builds and hot-development-server
* Yarn_ for js-dependencies
* Vue_ ready
* Caddy_ server with LetsEncrypt_ integration

Optional Integrations
---------------------

*These features can be enabled during initial project setup.*

* Integration with Travis_ for CI
* Integration with Sentry_ for error logging
* Integration with MailHog_ for local email testing
* Integration with YandexMetrika_ for web-analytics
* Integration with CKeditor_ for rich text editing

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
.. _YandexMetrika: https://tech.yandex.ru/metrika/
.. _CKeditor: https://ckeditor.com/
.. _Docker: https://www.docker.com/

Constraints
-----------

* Only maintained 3rd party libraries are used.
* Uses PostgreSQL everywhere (9.6).
* Environment variables for configuration.

Usage
------

Let's pretend you want to create a Django project called "redditclone". Rather than using `startproject`
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter_ to do all the work.

First, get Cookiecutter. Trust me, it's awesome::

    $ pip install "cookiecutter"

Now run it against this repo::

    $ cookiecutter https://github.com/vchaptsev/cookiecutter-django-vue

You'll be prompted for some values. Provide them, then a Django project will be created for you.

**Warning**: After this point, change 'Daniel Greenfeld', etc to your own information.

Answer the prompts with your own desired options. For example::

    project_name [Project Name]: My Awesome Website
    project_slug [my_awesome_website]: my_awesome_website
    author_name [Daniel Roy Greenfeld]: Your Name
    email [you@example.com]: author@myawesomewebsite.com
    description [A short description of the project.]: Description
    domain_name [example.com]: myawesomewebsite.com
    version [0.1.0]: 1.0
    timezone [UTC]: UTC
    language_code [en-us]: en-us
    Select open_source_license:
    1 - MIT
    2 - BSD
    3 - GPLv3
    4 - Apache Software License 2.0
    5 - Not open source
    Choose from 1, 2, 3, 4, 5 [1]: 1
    use_travis [y]: y
    use_sentry [y]: y
    use_mailhog [y]: y
    use_yandex_metrika [y]: y
    Select use_ckeditor:
    1 - Everywhere
    2 - Backend
    3 - Frontned
    4 - Don't use
    Choose from 1, 2, 3, 4 [1]: 1

Enter the project and take a look around::

    $ cd my_awesome_website/
    $ ls
