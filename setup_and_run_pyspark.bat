@echo off
REM ========== Activate Python Environment ==========
call E:\TempFolder\Desktop_21_07_2025\Python\50_Hrs_Big_Data_Mastery\big_data\Scripts\activate.bat

REM ========== Set Environment Variables ==========
set JAVA_HOME=C:\Java\jdk-11
set SPARK_HOME=C:\spark\spark-4.0.0-bin-hadoop3
set HADOOP_HOME=C:\hadoop
set PYSPARK_PYTHON=E:\TempFolder\Desktop_21_07_2025\Python\50_Hrs_Big_Data_Mastery\big_data\Scripts\python.exe
set PYSPARK_DRIVER_PYTHON=%PYSPARK_PYTHON%
set PATH=%JAVA_HOME%\bin;%SPARK_HOME%\bin;%HADOOP_HOME%\bin;%PATH%

REM ========== Navigate to project directory ==========
cd /d E:\TempFolder\Desktop_21_07_2025\Python\50_Hrs_Big_Data_Mastery

REM ========== Run PySpark script ==========
spark-submit PySpark\pyspark_01.py

pause
