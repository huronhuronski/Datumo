# syntax=docker/dockerfile:1

FROM python:3.7

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD [ "python", "app.py", "--host=0.0.0.0"]