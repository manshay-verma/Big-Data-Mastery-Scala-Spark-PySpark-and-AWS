from fastapi import FastAPI
from pyspark.sql import SparkSession

app = FastAPI()

@app.get("/")
def home():
    return {"message": "PySpark App is Live!"}

@app.get("/run")
def run_spark_job():
    # Create Spark Session
    spark = SparkSession.builder.appName("Intro").getOrCreate()

    # Sample Data
    data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
    df = spark.createDataFrame(data, ["Name", "Age"])

    # Collecting Data
    output_all = df.collect()
    output_filtered = df.filter(df.Age > 28).collect()
    total_rows = df.count()

    # Convert Row objects to dict for JSON response
    all_data = [row.asDict() for row in output_all]
    filtered_data = [row.asDict() for row in output_filtered]

    return {
        "all_data": all_data,
        "filtered_data": filtered_data,
        "total_rows": total_rows
    }
