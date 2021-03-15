FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install --upgrade pip

WORKDIR /app

COPY textabstractor /app/textabstractor
COPY ./setup.py /app
COPY textabstractor/app/main.py /app/main.py

RUN pip install .

