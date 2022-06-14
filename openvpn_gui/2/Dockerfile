FROM python:3.10-slim

WORKDIR /app

RUN apt update && apt install build-essential python-dev -y

ADD . /app

RUN python -m pip install -r ./requirements.txt

CMD ["uwsgi", "wsgi.ini"]