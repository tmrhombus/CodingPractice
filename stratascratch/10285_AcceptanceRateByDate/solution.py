
# Import your libraries
import pyspark
import pyspark.sql.functions as F

df_accept_status = (
    fb_friend_requests
    .groupBy("user_id_sender", "user_id_receiver")
    .agg(
        F.max(
            F.when( F.col("action")=="sent", 1).otherwise(0)    
        ).alias("was_sent"),
        F.max(
            F.when( F.col("action")=="accepted", 1).otherwise(0)    
        ).alias("was_accepted"),
        F.max(
            F.when( F.col("action")=="sent", F.col("date")).otherwise(None)  
        ).alias("dt_sent"),
    )
    .groupBy("dt_sent")
    .agg(
        F.sum("was_sent").alias("total_sent"),
        F.sum("was_accepted").alias("total_accepted")
    )
    .where(F.col("total_sent") > 0)
    .where(F.col("total_accepted") > 0)
    .withColumn("acceptance_rate",
        F.col("total_accepted")/F.col("total_sent")
    )
)

df_accept_status.select("dt_sent", "acceptance_rate").orderBy("dt_sent").toPandas()
