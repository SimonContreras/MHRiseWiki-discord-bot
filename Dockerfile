# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:alpine3.10

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Dependencies
RUN \
apk add --no-cache postgresql-libs && \
apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
apk add --no-cache bash

# Environment variables
# Discord token
ENV DISCORD_TOKEN=PUT YOUR TOKEN HERE

# pony ORM params
ENV PROVIDER_DB=postgres
ENV USER_DB=bot_mhrise
ENV PASSWORD_DB=Wvwd3Vu3YrxKPWsvd7EK
ENV HOST_DB=bot_db
ENV PORT_DB=5432
ENV DATABASE_NAME=mh_rise_wiki

# Assets for monster commands
ENV THUMBNAIL_ROUTE=./assets/thumbnail/

# Install pip requirements
COPY requirements.txt .
RUN pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# Working directory
WORKDIR /bot
COPY . /bot

# Run bot
CMD ["python", "main.py"]

