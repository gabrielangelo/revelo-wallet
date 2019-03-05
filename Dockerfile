FROM python:3.6

RUN mkdir /code
WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev

RUN pip install -U pip setuptools

COPY requirements.txt /code/

RUN mkdir ~/.ENVS

RUN pip install virtualenv

RUN virtualenv -p python3 ~/.virtualenvs/revelo

# RUN source ~/.virtualenvs/revelo/bin/activate

RUN pip install -r /code/requirements.txt

ADD . /code/