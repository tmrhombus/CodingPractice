
# Import your libraries
import pyspark
import pyspark.sql.functions as F
from pyspark.sql.window import Window


df_monthly_transactions = (
    sf_transactions
    .withColumn("month", F.date_format( F.col("created_at") , "yyyy-MM"))
    .groupBy("month")
    .agg(
        F.sum("value").alias("this_month_revenue")    
    )
    .withColumn( "last_month_revenue",
        F.lag("this_month_revenue", 1, None).over(
            Window.orderBy("month")    
        )
    )
    .withColumn("pct_diff",
        F.when(
            F.col("last_month_revenue") > 0,
            F.round( 
                100 * (F.col("this_month_revenue") - F.col("last_month_revenue")) / F.col("last_month_revenue")
            , 2)
        ).otherwise(None)
    )
)

df_out = df_monthly_transactions.select("month", "pct_diff").orderBy("month").toPandas()


