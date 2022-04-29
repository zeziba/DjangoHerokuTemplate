# pull official base image
FROM debian:11

# Enviroment settings
ARG SETUP_SCRIPT
ARG SCRIPTS_LOCATION

# set work directory
WORKDIR /usr/src/app

# Setup env for python
RUN apt-get update -y
RUN apt-get install -y python3.9 python3-pip curl

# Install Pyscopg2 dependencies
RUN apt-get install -y postgresql-server-dev-all gcc python3-dev musl-dev netcat

# Install NPM
RUN apt-get update && apt-get install -y \
    software-properties-common \
    npm
RUN npm install npm@latest -g && \
    npm install n -g && \
    n latest

# install dependencies  
RUN pip install --upgrade pip
COPY requirements.dev.txt .
# PyYAML causes errors on install ignoring it fixes this issue
RUN pip install --ignore-installed PyYAML
RUN pip install -r requirements.dev.txt

RUN npm install --prefix ./static/vendor bootstrap-sass bootstrap sass --save
RUN npm install --prefix ./static/vendor webpack webpack-cli --save-dev

# copy project
COPY . .

