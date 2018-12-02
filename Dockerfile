FROM python:3.6 
ENV PYTHONUNBUFFERED 1
RUN mkdir /3yourmind
WORKDIR /3yourmind
ADD requirements.txt /3yourmind/
RUN pip install -r requirements.txt
ADD . /3yourmind/