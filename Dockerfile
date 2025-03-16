FROM python:3.8.3-alpine

ADD . /mysite

WORKDIR /mysite
RUN pip3 install --upgrade pip

# Install build dependencies AND tzdata
RUN apk add --no-cache build-base python3-dev tzdata

RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD [ "python3.8", "./mysite/manage.py", "runserver", "0.0.0.0:8000" ]