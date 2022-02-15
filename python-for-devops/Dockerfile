FROM python:3.9.6-alpine3.13 as dev

WORKDIR /app

FROM python:3.9.6-alpine3.13 as debugging
# add debugger

FROM dev as runtime
COPY ./src/ /app

ENTRYPOINT [ "python", "/app/app.py" ]