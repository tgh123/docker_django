FROM python:3.7

LABEL maintaine = 'huazai'

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8

RUN mkdir /code
WORKDIR /code

RUN pip install pip -U

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/
