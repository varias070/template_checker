FROM python:3.8

WORKDIR app
RUN apt-get update
RUN mkdir -p -m 0700 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts
RUN apt install git
RUN --mount=type=ssh git clone git@github.com:varias070/template_checker.git
RUN cd template_checker && ls && \
    pip install -r requirements.txt
ENTRYPOINT cd template_checker && flask --app app.py run