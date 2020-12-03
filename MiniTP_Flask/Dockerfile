FROM alpine:latest

WORKDIR /usr/src/app

RUN apk update && apk add python3 && apk add py3-pip

COPY . .

RUN pip3 install -r requirements.txt

CMD python3 app.py
