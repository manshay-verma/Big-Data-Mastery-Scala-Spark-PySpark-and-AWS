from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Intro").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
df = spark.createDataFrame(data,["Name","Age"])

df.show()

df.filter(df.Age>28).show()

print("Total rows",df.count())