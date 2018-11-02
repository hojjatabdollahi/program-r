FROM python:3-onbuild
COPY . /usr/src/app
WORKDIR /usr/src/app
ENV PYTHONPATH="/usr/src/app/src:/usr/src/app/src/programy${PYTHONPATH}"
RUN pip install spacy
RUN pip install -r requirements.txt
RUN python -m spacy download en