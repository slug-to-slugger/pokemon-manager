FROM python:3.8

COPY Pipfile Pipfile.lock /

RUN pip install pipenv \
	&& pipenv install --system

ADD ./uwsgi/conf/pokemon_manager.ini /etc/uwsgi.d/pokemon_manager.ini

COPY ./pokemon_manager /var/www/app/pokemon_manager

WORKDIR /var/www/app/pokemon_manager

RUN python manage.py collectstatic --noinput

ENTRYPOINT ["sh", "/var/www/app/docker-entrypoint.sh"]