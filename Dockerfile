FROM ubuntu:latest
FROM python:3.10 as base
LABEL authors="roman"

#Set the working directory inside the container
WORKDIR /usr/src/app

#Upgrade pip, install pipenv, and configure pipenv
RUN pip install --upgrade pip && \
    pip install pipenv && \
    export PIPENV_VENV_IN_PROJECT=true && \
    pipenv install --ignore-pipfile


#Set the entry point to run pytest tests
ENTRYPOINT ["pipenv", "run", "pytest", "--alluredir", "allure-result", "-s", "-v"]

