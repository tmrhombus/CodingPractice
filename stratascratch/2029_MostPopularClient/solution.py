
# Import your libraries
import pyspark
import pyspark.sql.functions as F
from pyspark.sql.window import Window

valid_events = [
    "video call received",
    "video call sent", 
    "voice call received", 
    "voice call sent"
]

df_valid_users = (
    fact_events
    .groupBy("user_id")
    .agg(
        F.count("event_id").alias("nr_total_events"),
        F.sum(
            F.when( 
            F.col("event_type").isin(valid_events)    
            , 1).otherwise(0)    
        ).alias("nr_valid_events")
    )
    .withColumn("frac_valid_events",
        F.col("nr_valid_events")/F.col("nr_total_events")
    )
    .where(F.col("frac_valid_events") >= 0.5)
)

df_out = (
    fact_events
    .join(df_valid_users, on="user_id", how="inner")
    .groupBy("client_id")
    .agg(
        F.countDistinct("user_id").alias("nr_valid_users")    
    )
    .withColumn("rank",
        F.dense_rank().over(Window.orderBy(F.col("nr_valid_users").desc()))
    )
    .where(F.col("rank")==1)
)

df_out.select("client_id").toPandas()

