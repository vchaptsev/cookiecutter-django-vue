FROM python:3.6

ARG DJANGO_ENV=production
ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  PIPENV_SHELL_COMPAT=true \
  PIPENV_COLORBLIND=true \
  PIPENV_NOSPIN=true

COPY ./Pipfile /Pipfile
COPY ./Pipfile.lock /Pipfile.lock
RUN pip install pipenv && pipenv install --dev --system --ignore-pipfile

RUN groupadd -r django && \
  useradd -r -g django django

COPY ./compose/django/gunicorn.sh /gunicorn.sh
RUN sed -i 's/\r//' /gunicorn.sh && \
    chmod +x /gunicorn.sh && \
    chown django /gunicorn.sh

COPY ./compose/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh && \
    chmod +x /entrypoint.sh && \
    chown django /entrypoint.sh

COPY ./compose/django/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh && \
    chmod +x /start.sh && \
    chown django /start.sh

RUN mkdir -p /home/django/ && \
    touch /home/django/.ptpython_history && \
    sed -i 's/\r//' /home/django/.ptpython_history && \
    chmod +x /home/django/.ptpython_history && \
    chown django /home/django/.ptpython_history

COPY . /app
WORKDIR /app

RUN chown -R django /app
USER django

ENTRYPOINT ["/entrypoint.sh"]
