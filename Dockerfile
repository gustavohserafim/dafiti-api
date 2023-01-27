FROM python:3.10

WORKDIR /appl

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt update
RUN pip install --upgrade pip
COPY requirements.txt /appl/requirements.txt
RUN pip install -r ./requirements.txt --no-cache-dir
ADD . /appl
RUN chmod +x sources/entry-point.sh
RUN export FLASK_APP=wsgi.py
EXPOSE 5000
ENTRYPOINT ["/sources/entry-point.sh"]