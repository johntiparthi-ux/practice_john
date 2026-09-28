import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

options = PipelineOptions(streaming=True)

with beam.Pipeline(options=options) as pipeline:
    (
        pipeline
        | "CreateSampleData" >> beam.Create(["txn-001", "txn-002"])
        | "PrintTransactions" >> beam.Map(print)
    )
