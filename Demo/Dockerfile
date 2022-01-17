
FROM python:3.9-alpine3.13

ENV PYTHONUNBUFFERED = 1
 # Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE = 1 

RUN mkdir /Demo 
WORKDIR /Demo 
# Copy project from Host to Container
COPY . /Demo 

# must to set here rather than docker-compose.yml
ENV DJANGO_SETTINGS_MODULE=Demo.settings.prod
ENV SECRET_KEY=django-insecure-w1*7y5jovc#xyei65ixy6gc^y*k@^goom^xyh*#55gvbixapti


# Dependencies (pip ,PSQL ,Pillow) 
RUN pip install --upgrade pip && \
    apk update && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tem-deps \ 
        postgresql-dev gcc python3-dev musl-dev libpq postgresql-libs build-base libressl-dev libffi-dev linux-headers && \
    apk add jpeg-dev zlib-dev && \
    pip install -r requirements.txt && \
    apk del .tem-deps && \
    python manage.py collectstatic --noinput
    





