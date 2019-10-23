FROM python:3-alpine

RUN apk add nodejs npm
RUN npm install -g newman
RUN pip install -U Flask
