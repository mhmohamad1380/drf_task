FROM python:alpine
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD admin
ENV DJANGO_SUPERUSER_USERNAME admin
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir app
WORKDIR /app
COPY ./requirements.txt .
RUN apk add postgresql-client jpeg-dev
RUN apk add gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r requirements.txt
COPY . .