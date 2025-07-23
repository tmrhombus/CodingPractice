
# Import your libraries
import pyspark
import pyspark.sql.functions as F

# Start writing code
facebook_web_log = (
    facebook_web_log
    .where(F.col("action").isin(["page_load","page_exit"]))
    .withColumn("dt", F.to_date( "timestamp", "YY-MM-DD" ) )
    .groupBy("user_id", "dt")
    .agg(
        F.max(
            F.when(
                F.col("action")=="page_load", 
                F.col("timestamp")
            ).otherwise(None)
        ).alias("ts_page_load"),
        F.min(
            F.when(
                F.col("action")=="page_exit", 
                F.col("timestamp")
            ).otherwise(None)
        ).alias("ts_page_exit")
        )
    .where( F.col("ts_page_load").isNotNull() )
    .where( F.col("ts_page_exit").isNotNull() )
    .withColumn( "session_length", 
        F.unix_timestamp("ts_page_exit") - 
        F.unix_timestamp("ts_page_load") 
    )
    .where( F.col("session_length")>0 )
    .groupBy("user_id")
    .agg(
        F.avg("session_length").alias("avg_session_length")
        )
    )

# To validate your solution, convert your final pySpark df to a pandas df
facebook_web_log.toPandas()
