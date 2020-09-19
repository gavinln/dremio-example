# dremio-example

* Source code - [Github][1]
* Author - Gavin Noronha - <gavinln@hotmail.com>

[1]: https://github.com/gavinln/dremio-example

## About

## Setup

### Start Dremio in Docker

1. Start the Docker daemon

```
sudo service docker start
```

2. Change to the Dremio directory

```
cd dremio
```

3. Start Dremio

```
docker-compose up -d
```

4. Display services

```
docker-compose ps
```

5. Display server address

```
hostname -I
```

6. Connect to Dremio server at http://localhost:9047/

7. Setup the user: gavinln, password: dremio-pass1

## Links

* Dremio [ports][1000]

[1000]: https://docs.dremio.com/deployment/system-requirements.html#network

* Dremio [sqlalchemy][1010]

[1010]: https://github.com/narendrans/sqlalchemy_dremio

* Dremio [arrow flight][1020]

[1020]: https://github.com/dremio-hub/dremio-flight-connector
