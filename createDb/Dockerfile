FROM alpine:latest

RUN apk update && \
    apk add mysql && \
    apk add mysql-client

COPY init.sql ./init.sql

WORKDIR .
ADD . .

CMD mysql -u root -p'example' -h db -P3306 -D sys < init.sql



