FROM python:3.8

COPY Pipfile Pipfile.lock /

RUN pip install pipenv \
	&& pipenv install --system

COPY ./pokemon_manager /var/www/pokemon_manager

WORKDIR /var/www/pokemon_manager

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]