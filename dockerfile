FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /CI-CD-DRF
WORKDIR /CI-CD-DRF

COPY requirements.txt /CI-CD-DRF/

RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . /CI-CD-DRF/

RUN ls -a
