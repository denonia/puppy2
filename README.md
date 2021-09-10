![perro](assets/perro.png)

# features
* nothing (yet)

# docker 

1. clone this repository
```bash
git clone https://github.com/denonia/puppy2.git && cd puppy2
```

2. set **TOKEN_TELEGRAM** in .env file
```bash
TOKEN_TELEGRAM=1234567890:something > .env
```
3. build the container
```bash
docker-compose up --build -d
```

* to stop and remove existing container run
```bash
docker-compose down --rmi all
```
* stop existing container without removing
```bash
docker-compose down
```
* start existing container
```bash
docker-compose up -d
```

