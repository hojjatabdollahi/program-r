FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev net-tools\
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata  
  
COPY . /usr/src/app
WORKDIR /usr/src/app
ENV PYTHONPATH="/usr/src/app/src:/usr/src/app/src/programy${PYTHONPATH}"
RUN pip install spacy
RUN pip install -r requirements.txt
RUN python -m spacy download en
CMD ["python", "./src/programy/clients/events/majordomo/client.py", "--config", "./bots/ryan/config.yaml", "--cformat", "yaml", "--logging", "./bots/ryan/logging.yaml"]