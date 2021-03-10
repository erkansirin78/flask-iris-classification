FROM python:3.6
COPY . /opt/
WORKDIR /opt
RUN pip install -r requirements.txt
ENTRYPOINT FLASK_APP=app.py flask run --host=0.0.0.0 --port=8080

