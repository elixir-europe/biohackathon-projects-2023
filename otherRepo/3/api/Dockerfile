FROM python:3.10.13-alpine3.18 as BUILD

RUN apk add --update \
    && apk add --no-cache --virtual build-base libressl-dev libffi-dev gcc musl-dev python3-dev \
    && rm -rf /var/cache/apk/*

COPY requirements.txt /root/requirements.txt

RUN pip install --upgrade pip && \
    pip install -r /root/requirements.txt

FROM python:3.10.13-alpine3.18

RUN apk add --no-cache --update bash

COPY --from=BUILD /usr/local/lib/python3.10/ /usr/local/lib/python3.10/

COPY --from=BUILD /usr/local/bin/uvicorn /usr/local/bin/

RUN mkdir -p /app

WORKDIR /app

COPY ./app.sh /app/app.sh

COPY ./main.py /app/main.py

COPY ./data.json /app/data.json

RUN chmod +x /app/app.sh

RUN addgroup -g 1001 app && \
    adduser -D -u 1001 --disabled-password \
    --no-create-home -G app app

ENTRYPOINT ["/bin/sh", "-c", "/app/app.sh"]
