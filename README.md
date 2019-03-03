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

1. Create an .env file and set variables. Examples can be found in `local.env`.

2. Create a virtual environment:

```
$ virtualenv <env_name>
$ source <env_name>/bin/activate
```

3. Installation:

```
$ make setup
```

4. Start the server:

```
$ make run
```

The site will be available on <http://127.0.0.1:8000>.


## REST API Docs

REST API docs can be found in <http://127.0.0.1:8000/api/v1/docs/>.


## Deploy

To deploy to heroku:

1. Create a project in Heroku
2. Add a Postgres database
3. Set environment variables
4. Push to the Heroku repository:

```
$ git push heroku master
```

5. Run migrations:

```
$ heroku run python manage.py migrate
```

## Authors

* **Gabriel Angelo** - [gabrielangelo](https://github.com/gabrielangelo/)

