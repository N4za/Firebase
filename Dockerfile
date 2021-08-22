  
FROM ubuntu:20.04

LABEL description = "Docker Hub"
LABEL mainteiner = "Nazareth MR"
LABEL version = "v1"

RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN pip install web.py
RUN pip install pyrebase