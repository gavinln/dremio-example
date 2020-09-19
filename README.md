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

### Install ODBC

1. Install ODBC drivers

```
sudo apt install -y unixodbc unixodbc-dev
```

2. Download Dremio ODBC driver

```
wget https://download.dremio.com/odbc-driver/dremio-odbc-LATEST.x86_64.rpm
```

3. Install alien to convert from rpm to deb

```
sudo apt install alien
```

4. Convert to debian

Copy to the home directory

```
alien --to-deb dremio-odbc-LATEST.x86_64.rpm
```

5. Install the deb file

```
sudo dpkg -i drmeio-odbc-xxxxxx.deb
```

A file /opt/dremio-odbc/conf/odbcinst.ini will be created.

###  Setup dremio cache

1. Create a directory for the Dremio data

```
mkdir ~/dremio_data
```

2. Set the owner of the directory

```
chown username:docker dremio_data
```

3. Make sure the directory is writable by the group

```
chmod g+w dremio_data
```

4. The ./dremio/docker-compose.yml file has the following setting

```
volumes:
    - "/home/username/dremio_data:/opt/dremio/data"
    ```

## Links

### Dremio

* Dremio [ports][1000]

[1000]: https://docs.dremio.com/deployment/system-requirements.html#network

* Dremio [sqlalchemy][1010]

[1010]: https://github.com/narendrans/sqlalchemy_dremio

* Dremio [arrow flight][1020]

[1020]: https://github.com/dremio-hub/dremio-flight-connector

### General data engineering

* [Data trends][1300] for 2020

[1300]: https://www.youtube.com/watch?v=Os0MO9SHS3M

* Netflix [big data cloud storage][1310]

[1310]: https://www.youtube.com/watch?v=9uiaCN3tJyI


