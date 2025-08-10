
# Import your libraries
import pyspark
import pyspark.sql.functions as F

df_process_rate = (
    facebook_complaints
    .groupBy("complaint_id")
    .agg(
        F.mode("type").alias("type"),
        F.max("processed").alias("processed")
    )
    .groupBy("type")
    .agg(
        F.count("complaint_id").alias("nr_complaints"),
        F.sum(
            F.when( F.col("processed")==True, 1 ).otherwise(0)
        ).alias("nr_processed")
    )
    .withColumn( "processed_frac",
        F.round(  F.col("nr_processed")/F.col("nr_complaints") ,2 )
    )
)


df_process_rate.select("type", "processed_frac").toPandas()


