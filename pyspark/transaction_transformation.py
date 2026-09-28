from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("TransactionTransformation").getOrCreate()

df = spark.read.option("header", True).option("inferSchema", True).csv("transactions.csv")

clean_df = df.filter(col("amount") > 0)

clean_df.show()
spark.stop()
