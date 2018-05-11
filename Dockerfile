FROM python:3.6.5-alpine3.7
MAINTAINER Felipe Colen <felipecolen@gmail.com>

WORKDIR /usr/src/app
COPY . .
RUN rm -rf .git .idea .libs *.log

RUN python3 -m ensurepip && \
    pip install --upgrade pip setuptools

RUN pip install --no-cache-dir -r requirements.txt

RUN rm -r /root/.cache

EXPOSE 5000
