import os
os.environ["HADOOP_HOME"] = "C:\\hadoop"

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SparkTest") \
    .master("local[2]") \
    .getOrCreate()

print("================================")
print("SPARK WORKING SUCCESSFULLY!")
print("================================")

spark.stop()