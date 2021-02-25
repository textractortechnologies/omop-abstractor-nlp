FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install --upgrade pip

WORKDIR /app

COPY ./abstractor /app/abstractor
COPY ./setup.py /app
COPY ./abstractor/app/main.py /app/main.py

RUN pip install .

