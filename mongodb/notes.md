## install
docker pull mongo:4.4.4

## run 
docker container run --name smoke-mongo -d --rm mongo:4.4.4

## connect
docker container exec -it smoke-mongo /bin/sh

## create db
```bash
mongo
use smoke
db.endpoints

endpoint1 = {
    "name": "response-200",
    "requests": 4,
    "timeout": 5,
    "url": "https://httpbin.org/status/200"
}

endpoint2 = {
    "name": "response-404",
    "requests": 3,
    "timeout": 3,
    "url": "https://httpbin.org/status/404"
}

db.endpoints.insertMany([endpoint1, endpoint2])

show dbs

db.endpoints.find()
db.endpoints.find({name: "response-200"})
```