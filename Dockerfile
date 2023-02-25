# define image 
FROM python:3.10-slim-buster

# defining the maintainer
LABEL maintainer="bigdeli.ali3@gmail.com"

ENV PYTHONUNBUFFERED=1


# setting working directory
WORKDIR /usr/src/app


# adding gettext package
RUN apt-get update
RUN apt-get install gettext -y
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

# copying requirement files
COPY requirements.txt .

# installing packages
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# copy project directory
COPY ./core .
