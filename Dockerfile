FROM python:2.7-slim
MAINTAINER Kunle Kolawole <ksquare267@gmail.com>

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev --no-install-recommends

ENV INSTALL_PATH /quest
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable .

CMD gunicorn -c "python:config.gunicorn" "quest.app:create_app()"
