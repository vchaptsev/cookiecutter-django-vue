{{cookiecutter.project_name}}
{{ '=' * cookiecutter.project_name|length }}

{{cookiecutter.description}}

  <a href="https://github.com/vchaptsev/cookiecutter-django-vue">
      <img src="https://img.shields.io/badge/built%20with-Cookiecutter%20Django%20Vue-blue.svg" />
  </a>

  {% if cookiecutter.license != "Not open source" %}
  ## License
  {{cookiecutter.license}}
  {% endif %}
