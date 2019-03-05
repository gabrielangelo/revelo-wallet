# Cerelo wallet

## Main tools used in this project

* Ubuntu 16.04 LTS
* Visual Studio Code
* Python 3.5.2
* Django 2.1.7
* Django REST Framework 0.1.0


## Getting Started

### Prerequisites

* Python 3.5.2
* Postgres 9.3.15 (optional but recommended)


### Installing

1. Create a virtual environment:

```
$ virtualenv <env_name>
$ source <env_name>/bin/activate


```
2. Set PROJECT var in Makefile to your virtualenv name (<env_name> above), after this, set VENV var with the directory name of your virtualenv:
```
PROJECT := <env_name>
VENV := ~/.virtualenvs 
```
3. Installation:

```
$ make setup
```

4. Start the server:

```
$ make run
```

## Using docker
1. set DATABASES 'HOST' value in revelowallet/settings/local.py file to 'db' 
2. Run:
```
$ make init-docker-app
$ make up_container
```
3. To close down the Docker container:
```
$ make down_container
```
The site will be available on <http://localhost:8000>.


## REST API Docs

REST API docs can be found in <http://localhost:8000/api/v1/docs/>.


## Deploy

To deploy to heroku:

1. Create a project in Heroku
2. Add a Postgres database
3. Set environment variables at .env file
4. Push to the Heroku repository:

```
$ git push heroku master
```

5. Run migrations and populate database:

```
$ heroku run python manage.py migrate && python manage.py populate_db
```

## Authors

* **Gabriel Angelo** - [gabrielangelo](https://github.com/gabrielangelo/)

