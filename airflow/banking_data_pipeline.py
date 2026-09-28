from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def validate_file():
    print("Checking source file")

with DAG(
    dag_id="banking_data_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    start_pipeline = EmptyOperator(task_id="start_pipeline")
    check_file = PythonOperator(
        task_id="check_file",
        python_callable=validate_file,
    )
    end_pipeline = EmptyOperator(task_id="end_pipeline")

    start_pipeline >> check_file >> end_pipeline
