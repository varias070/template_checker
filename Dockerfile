FROM python:3.8

WORKDIR app
RUN apt-get update
COPY requirements.txt requirements.txt
RUN mkdir -p -m 0700 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts
RUN pip install -r requirements.txt && apt install git
RUN --mount=type=ssh git clone git@github.com:rosstrah/spider_tinkoff.git