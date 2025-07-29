
# Import your libraries
import pyspark
import pyspark.sql.functions as F

themonth = "2019 03"
df_revenue = (
    orders
    .withColumn("trans_month", F.date_format("order_date", "yyyy MM"))
    .where(F.col("trans_month") == themonth)
    .groupBy("cust_id")
    .agg(
        F.sum("total_order_cost").alias("revenue")    
    )
)

df_revenue.select("cust_id", "revenue").orderBy(F.col("revenue").desc()).toPandas()
