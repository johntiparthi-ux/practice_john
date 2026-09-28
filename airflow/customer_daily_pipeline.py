from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id="customer_daily_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    start = EmptyOperator(task_id="start")
    load_customer = EmptyOperator(task_id="load_customer")
    validate_customer = EmptyOperator(task_id="validate_customer")
    finish = EmptyOperator(task_id="finish")

    start >> load_customer >> validate_customer >> finish
