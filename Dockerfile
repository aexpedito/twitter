FROM ubuntu:20.04

##install python 
RUN apt-get update
RUN apt-get install -y python3-pip python3-venv virtualenv tmux

#SET VARIABLES
ENV CONSUMER_KEY=
ENV CONSUMER_SECRET=
ENV ACCESS_KEY=
ENV ACCESS_SECRET=
ENV FLASK_APP=twitter.py

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1

ENV APP_HOME /usr/src/app
WORKDIR /$APP_HOME

COPY . $APP_HOME/

RUN pip3 install -r requirements.txt
RUN python3 -m textblob.download_corpora

EXPOSE 8080


CMD gunicorn -b 0.0.0.0:8080 -w 2 twitter:app


