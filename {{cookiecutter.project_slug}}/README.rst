{{cookiecutter.project_name}}
{{ '=' * cookiecutter.project_name|length }}

{{cookiecutter.description}}

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django%20Vue-blue.svg
     :target: https://github.com/vchaptsev/cookiecutter-django-vue/
     :alt: Built with Cookiecutter Django Vue

{% if cookiecutter.license != "Not open source" %}

:License: {{cookiecutter.license}}
{% endif %}
