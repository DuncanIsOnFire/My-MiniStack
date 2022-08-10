FROM python:3.10.6-alpine3.16
RUN mkdir -p /app
WORKDIR /app

COPY ./src/ /app/
RUN pip install -r requirements.txt

ENV FLASK_APP=app.py

EXPOSE 5000

CMD flask run -h 0.0.0.0 -p 5000
