
# Import your libraries
import pyspark
import pyspark.sql.functions as F
from pyspark.sql.window import Window

df_most_flagged = (
    user_flags
    .groupBy("video_id")
    .agg(
        F.countDistinct("flag_id").alias("nr_user_flags")
    )
    .withColumn("flag_rank",
        F.dense_rank().over(
            Window.orderBy(F.col("nr_user_flags").desc())    
        )
    )
    .where(F.col("flag_rank")==1)
)

df_out = (
    user_flags
    .join(df_most_flagged, on="video_id", how="inner")
    .join(flag_review.withColumn("isReviewed", 
        F.when(F.col("reviewed_by_yt"), 1).otherwise(0)
        )
        , on="flag_id", how="left")
    .fillna(0)
    .groupBy("video_id")
    .agg(
        #F.count("flag_id").alias("nr_flags_total")
        F.sum("isReviewed").alias("nr_flags_reviewed")    
    )
)

df_out.toPandas()



