FROM python:3.8

COPY Pipfile Pipfile.lock /

RUN pip install pipenv \
	&& pipenv install --system

ADD ./uwsgi/conf/pokemon_manager.ini /etc/uwsgi.d/pokemon_manager.ini

COPY ./app /var/www/app

WORKDIR /var/www/app

RUN python manage.py collectstatic --noinput

ENTRYPOINT ["sh", "/var/www/app/docker-entrypoint.sh"]