FROM python:3

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
RUN pip install flask-cors --upgrade

WORKDIR /src/