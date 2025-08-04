## Load Data 
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("JoinsExample").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

empolyees = spark.read.csv(r"PySpark/csv/employees.csv",header=True,inferSchema=True)
department = spark.read.csv(r"PySpark/csv/departments.csv",header=True,inferSchema=True)

empolyees.show()
department.show()

# Perform Joins
emp_dept = empolyees.join(department, on = "DeptID",how="inner")
emp_dept.show()

# Aggregations 
## Average Salary Department
from pyspark.sql import functions as F

avg_salary = emp_dept.groupBy("DeptName").agg(F.avg("Salary").alias("AvgSalary"))
avg_salary.show()

## Maximum Salary in Company
max_salary = empolyees.agg(F.max("Salary").alias("MaxSalary"))
max_salary.show()

## Sort & Save 
avg_salary.orderBy(F.desc("AvgSalary")).show()

### SAVE 
avg_salary.write.csv("avg_salary_by_dept",header=True, mode="overwrite")

