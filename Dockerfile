FROM python:3.8-slim-buster

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY ./app.py /app/app.py

RUN pip install -r requirements.txt

# Create a folder for storage
RUN mkdir /data

ENTRYPOINT ["python", "app.py"]
