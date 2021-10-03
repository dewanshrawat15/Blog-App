FROM python:3.8.3-alpine

ADD . /mysite

WORKDIR /mysite

RUN pip3 install -r docker-requirements.txt

CMD [ "python3.8", "./mysite/manage.py", "runserver", "0.0.0.0:8000" ]