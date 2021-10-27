# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

COPY . /app/src/python-flask
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app/src/python-flask

CMD [ "python3", "server.py"]
