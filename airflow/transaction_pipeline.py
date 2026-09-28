from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id="transaction_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@hourly",
    catchup=False,
) as dag:

    start = EmptyOperator(task_id="start")
    ingest = EmptyOperator(task_id="ingest")
    transform = EmptyOperator(task_id="transform")
    load_bq = EmptyOperator(task_id="load_bq")
    finish = EmptyOperator(task_id="finish")

    start >> ingest >> transform >> load_bq >> finish
