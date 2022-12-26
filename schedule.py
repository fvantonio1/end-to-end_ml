import datetime
import yfinance as yf
from sklearn.linear_model import LinearRegression
import numpy as np
from joblib import dump
import datetime as dt

from airflow.models import DAG
from airflow.operators.python import PythonOperator

WORFKLOW_DAG_ID = "train_model_dag"
WORFKFLOW_START_DATE = datetime.datetime(2022, 1, 1)
WORKFLOW_SCHEDULE_INTERVAL = "0 * * * *"
WORKFLOW_EMAIL = ["fv.antonio@yahoo.com"]

WORKFLOW_DEFAULT_ARGS = {
    "owner": "antonio",
    "start_date": WORFKFLOW_START_DATE,
    "email": WORKFLOW_EMAIL,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
}
# Initialize DAG
dag = DAG(
    dag_id=WORFKLOW_DAG_ID,
    schedule=WORKFLOW_SCHEDULE_INTERVAL,
    default_args=WORKFLOW_DEFAULT_ARGS,
)

def job_1():
    BTC_Ticker = yf.Ticker("BTC-USD")
    data = BTC_Ticker.history(period="max")

    X = data.index.map(dt.datetime.toordinal).values

    reg = LinearRegression()
    reg.fit(X.reshape(-1,1), y=data['Close'].values)

    dump(reg, 'models/model.joblib')

job_1_operator = PythonOperator(
    task_id = "train_model",
    python_callable=job_1,
    dag=dag
)