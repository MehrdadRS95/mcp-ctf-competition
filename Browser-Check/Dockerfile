FROM python:3.13.4-slim-bookworm
COPY . /srv/
WORKDIR /srv/
RUN apt update
RUN apt update
RUN apt install build-essential libssl-dev wget -y
RUN pip3 install -r requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:5555", "-w", "1", "--threads", "4", "chall:http", "--certfile=cert.pem", "--keyfile=key.pem"]