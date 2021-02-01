FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /usr/src/app

COPY . .

RUN apt-get update && apt-get install -y \
    vim \
    python \
    python-pip
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "5000"]