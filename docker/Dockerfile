FROM python:3.8.7

EXPOSE 8080

CMD supervisord -c /etc/supervisord.conf

WORKDIR /app

ARG FLASK_ENV
ARG SECRET_KEY_BASE

ENV FLASK_ENV ${FLASK_ENV}
ENV SECRET_KEY_BASE ${SECRET_KEY_BASE}

RUN set -eux && \
    apt-get update -qqy && \
    apt-get install -qqyy gcc mono-mcs supervisor nginx libboost-dev libboost-program-options-dev cmake && \
    rm -rf /var/lib/apt/lists/*

COPY docker/supervisord.conf /etc/supervisord.conf
COPY docker/nginx.conf /etc/nginx/sites-available/default

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

RUN bin/build
