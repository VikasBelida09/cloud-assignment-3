FROM alpine:latest

RUN mkdir home/data
ADD IF.txt home/data/
ADD Limerick.txt home/data/
ADD app.py /home

RUN apk update && \
    apk add --no-cache python3

CMD ["/home/app.py"]
ENTRYPOINT [ "python3" ]