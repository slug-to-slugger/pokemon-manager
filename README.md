# POKEMON MANAGER

## For development

### Build container

```sh
docker-compose build
```

### Run container

```sh
docker-compose up -d
```

### Insert Pokemon master data (Every time DB data initialized)

```sh
docker exec -t pokemon_manager python manage.py makemigrations pokemon
docker exec -t pokemon_manager python manage.py migrate
docker exec -t pokemon_manager /bin/sh loaddata.sh
```


## Request sample

```sh
# Get auth token
curl -H 'Content-Type: application/json' http://localhost/api-token-auth/ -d '{"username": "test", "password": "test"}'
# {"token":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

# Get trainer list
curl http://localhost/trainers/

# Post trainer
curl -H 'Content-Type: application/json' http://localhost/trainers/ -d '{"username": "test", "password": "test", "login_id": "test@example.com"}'
```
