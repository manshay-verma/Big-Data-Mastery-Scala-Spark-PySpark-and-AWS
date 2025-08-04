from pyspark.sql import SparkSession
from pyspark.sql import functions as F 

spark = SparkSession.builder.appName("MiniETLProject").getOrCreate()

## Extract load csv + JSON
employees = spark.read.csv(r"PySpark/csv/employees.csv",header=True, inferSchema=True)
departments = spark.read.json(r"PySpark/csv/departments.json")

print("Employees Data:")
employees.show()

print("Departments Data:")
departments.show()

## TRANSFORM Clean & Join 
### Join on DeptID
emp_dept = employees.join(departments, on = "DeptID", how="inner")

### Add Bonus Columns = 10% of Salary
emp_dept = emp_dept.withColumn("Bonus",(F.col("Salary")*0.10))

### Compute AvgSalary by Dept
avg_salary = emp_dept.groupBy("DeptName").agg(
    F.avg("Salary").alias("AvgSalary"),
    F.count("EmpID").alias("TotalEmployees")
)

#### Show Result 
print("Join Employee + Department Data:")
emp_dept.show()

print("Avg Salary By Department:")
avg_salary.show()

## Load: Save as Parquet (optimized for Big Data)
emp_dept.write.mode("overwrite").parquet("output/emp_dept_parquet")
emp_dept.write.mode("overwrite").json("output/avg_salary_json")

