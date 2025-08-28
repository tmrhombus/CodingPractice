
# Import your libraries
import pyspark
import pyspark.sql.functions as F
from pyspark.sql.window import Window

# Start writing code
df_daily_hpu = (
    cust_tracking    
    .withColumn( "dt", F.date_format(F.col("timestamp"), "yyyy-MM-dd") )
    .withColumn( "ts", F.unix_timestamp(F.col("timestamp")) )
    .withColumn("next_ts", 
        F.lead("ts", 1, None).over(
            Window.partitionBy("cust_id").orderBy("ts")    
        )
    )
    .withColumn("ts_diff",
        F.when(F.col("state")==1, 
            (F.col("next_ts")-F.col("ts"))/3600
        ).otherwise(0)
    )
    .groupBy("dt", "cust_id")
    .agg(
        F.sum("ts_diff").alias("hpu")    
    )
)

df_daily_hpu.select("cust_id", "hpu").orderBy("cust_id").toPandas()


