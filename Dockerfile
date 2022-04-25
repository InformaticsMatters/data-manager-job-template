FROM python:3.10.4-alpine3.15

ENV PYTHONUNBUFFERED=1
ENV HOME=/code

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

WORKDIR ${HOME}
COPY src/ ./
