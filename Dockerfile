FROM python:3.7.4-slim

RUN mkdir /data/

WORKDIR /data

COPY ./SoftEng/ ./
COPY ./requirements.txt .

RUN pip install -r ./requirements.txt
