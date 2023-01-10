FROM python:3.8
WORKDIR app
COPY . ./
RUN pip install -r requirements.txt
CMD flask --app app.py run -h 0.0.0.0