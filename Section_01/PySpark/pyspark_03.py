from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ReadCSVExample").getOrCreate()

df = spark.read.csv(r"PySpark/csv/people.csv", header=True, inferSchema=True)

df.show()

df.printSchema()

df.select("Name","City").show()

df.filter(df.Age > 30).show()

df.groupBy("City").count().show()

df.orderBy(df.Age.desc()).show()

df.filter(df.Age>30)\
    .write \
    .csv("PySpark/output_folder",header=True,mode="overwrite")