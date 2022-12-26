FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD airflow db init; cp schedule.py /python-docker/venv/lib/python3.8/site-packages/airflow/example_dags/;python3 -m flask run --host=0.0.0.0