# FROM python:3.8-alpine
FROM python@sha256:c3d944675b54439bad2f6f7a766fe77dffd3e0af2cf0a9fb99d27df75e740a33

ENV PORT 59909

# Add files
COPY app /app
COPY flag requirements.txt /

# Install dependencies
RUN apk add --no-cache --virtual .build-deps build-base \
 && pip install --no-cache-dir -r /requirements.txt \
 && rm -f /requirements.txt \
 && apk del .build-deps

WORKDIR /app
RUN python manage.py migrate tablet 0001
RUN chmod +x run.sh

CMD ["./run.sh"]
EXPOSE $PORT
