FROM ubuntu:latest

ADD IF.txt home/data/
ADD Limerick.txt home/data/
ADD app.py /home

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
	python3

WORKDIR /home
RUN python3 app.py

WORKDIR /home/output

CMD ["cat","result.txt"]