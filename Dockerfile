FROM python:3.7.4-slim

RUN mkdir /data/

WORKDIR /data
RUN apt-get update
RUN apt-get install -y default-libmysqlclient-dev gcc python-dev
COPY ./requirements.txt .

RUN pip install -r ./requirements.txt

COPY ./SoftEng/ ./