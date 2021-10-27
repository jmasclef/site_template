# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

COPY ./src /app/src
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app/src

CMD [ "python3", "server.py"]
