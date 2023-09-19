#FROM ubuntu:latest
#LABEL authors="nastyaizofatova"
#
#ENTRYPOINT ["top", "-b"]

FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip --no-cache-dir && pip install --no-cache-dir -r requirements.txt

COPY . .