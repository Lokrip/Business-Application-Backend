FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY service /service
WORKDIR /service
EXPOSE 8000

#это нужно чтобы мы могли подключаться нормально к postgresql через linux тоесть установка необходимых зависимостей
# RUN apt-get update && apt-get install -y \
#     postgresql-client \
#     build-essential \
#     libpq-dev && \
#     rm -rf /var/lib/apt/lists/*

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password service-user

USER service-user
