FROM python:3.7-alpine
LABEL org.opencontainers.image.authors="samodelkinas@gmail.com"
ENV PYTHONUNBUFFERED 1
RUN apk add build-base jpeg-dev zlib-dev
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN mkdir /app
WORKDIR /app
COPY ./app /app/
RUN adduser -D user
USER user
ENTRYPOINT python manage.py runserver 0.0.0.0:8000