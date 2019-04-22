FROM python:3.7

RUN mkdir /src
RUN pip install flask requests aws-xray-sdk

ADD ./src /src
WORKDIR /src

