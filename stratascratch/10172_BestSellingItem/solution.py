
# Import your libraries
import pyspark
import pyspark.sql.functions as F
from pyspark.sql.window import Window

# Start writing code

df_totals = (
    online_retail
    .withColumn("month", F.date_format(F.col("invoicedate"),  "MM"))
    .withColumn("transaction_spend", F.col("unitprice")*F.col("quantity"))
    .groupBy("month", "description")
    .agg(
        F.sum("transaction_spend").alias("monthly_spend")    
    )
    .withColumn( "monthly_rank",
        F.dense_rank().over(
            Window.partitionBy("month").orderBy(F.col("monthly_spend").desc())    
        )
    )
    .where(F.col("monthly_rank") == 1 )
)


df_out = df_totals.select("month", "description", "monthly_spend").orderBy("month")
df_out.toPandas()


