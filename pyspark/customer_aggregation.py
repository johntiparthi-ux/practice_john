from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as spark_sum

spark = SparkSession.builder.appName("CustomerAggregation").getOrCreate()

df = spark.read.option("header", True).option("inferSchema", True).csv("transactions.csv")

result = df.groupBy("customer_id").agg(
    spark_sum("amount").alias("total_amount")
)

result.show()
spark.stop()
