from google.cloud import bigquery

def load_table(project_id, dataset_id, table_id, source_uri):
    client = bigquery.Client(project=project_id)
    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
    )

    job = client.load_table_from_uri(source_uri, table_ref, job_config=job_config)
    job.result()
    print(f"Loaded data into {table_ref}")
