FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev net-tools nano vim\
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
  && pip3 install setuptools
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata  
  
COPY . /usr/src/app
WORKDIR /usr/src/app
ENV PYTHONPATH="/usr/src/app/src:/usr/src/app/src/programr${PYTHONPATH}"
RUN pip install --upgrade setuptools
RUN pip install spacy
RUN pip install -r requirements.txt
RUN python -m spacy download en
RUN chmod +x run.sh
RUN sed -i -e 's/\r$//' run.sh