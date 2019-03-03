PROJECT := revelo
PYTHON_BIN := python
VENV := ~/.ENVS/$(PROJECT)
PYTHON_PATH := $(VENV)/bin/$(PYTHON_BIN)
MANAGE := $(PYTHON_PATH) manage.py
MANAGE_TEST := $(MANAGE) test


profile:
	$(MANAGE) runserver --nothreading

run:
	$(MANAGE) runserver 0.0.0.0:8000

shell:
	$(MANAGE) shell_plus

shell-sql:
	$(MANAGE) shell_plus --print-sql

urls:
	$(MANAGE) show_urls

urls-api:
	$(MANAGE) show_urls | grep -i api

test:
	$(MANAGE_TEST)

test_wallet:
	$(MANAGE_TEST) wallet

migrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

showmigrations:
	$(MANAGE) showmigrations

setup:
	@pip install -r requirements/prod.txt
	$(MANAGE) migrate
	$(MANAGE_TEST)
	$(MANAGE) populate_db

pop_db:
	$(MANAGE) populate_db

clean:
	@find . -name "*.pyc" -delete

install_local_deps:
	@pip install requirements/local.txt 

install_prod_deps:
	@pip install requirements/prod.txt

help:
	grep '^[^#[:space:]].*:' Makefile | awk -F ":" '{print $$1}'

