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
curl -H "Content-Type: application/json" http://localhost/api-token-auth/ -d '{"username": "test", "password": "test"}'
# {"token":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

# Set token to environment
export POKEMON_API_TOKEN='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# Get trainer list
curl http://localhost/trainers/

# Get trainer detail
curl -H "Authorization: Token ${POKEMON_API_TOKEN}" http://localhost/trainers/<trainer_id>/

# Post trainer
curl -H "Content-Type: application/json" http://localhost/trainers/ -d '{"username": "test", "password": "test", "login_id": "test@example.com"}'

# Get partner list
curl -H "Authorization: Token ${POKEMON_API_TOKEN}" http://localhost/pokemons/

# Post partner list
curl -H "Content-Type: application/json" -H "Authorization: Token ${POKEMON_API_TOKEN}" http://localhost/pokemons/ -d '{"name": "<ニックネーム: string>", "ability": "<特性: string>", "character": "<性格: string>", "gender": <1=♂ 2=♀ 3=その他: integer>, "h": <0 ~ 252: integer>, "a": <0 ~ 252: integer>, "b": <0 ~ 252: integer>, "c": <0 ~ 252: integer>, "d": <0 ~ 252: integer>,  "s": <0 ~ 252: integer>, "pokemon_id": "<図鑑番号: integer>"}'

# Get partner detail
curl -H "Authorization: Token ${POKEMON_API_TOKEN}" http://localhost/pokemons/<partner_id>/
```
