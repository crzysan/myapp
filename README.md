# Overview

* Build a django app docker image

# How to Run
## Clone this repo
```
git clone https://github.com/crzysan/myapp.git
```

## From DockerHub

Pulling the image
```
docker pull crzysan/myapp
```

## Building the image for the first time
```
docker build . -t crzysan/myapp:v1
```

## Run the container
```
docker run -d crzysan/myapp:v1
docker run --name myapp -p 8000:8000 -d crzysan/myapp:v1
```

## Connect to the container
```
docker exec -it myapp /bin/bash
