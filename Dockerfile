FROM alpine:latest

RUN apk add --update python py-pip
RUN pip install scapy requests

ADD dash_listener.py dash_listener.py

CMD ["python", "-u", "dash_listener.py"]
