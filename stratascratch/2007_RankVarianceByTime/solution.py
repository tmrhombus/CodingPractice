
# Import your libraries
import pyspark
import pyspark.sql.functions as F
from pyspark.sql.window import Window

month1 = "2019 12"
month2 = "2020 01"
list_months = [month1, month2]    
    
## Count Nr Comments per Month
df_comments_per_month = (
    fb_comments_count
    .withColumn("month", F.date_format("created_at", "yyyy MM") )
    .where(F.col("month").isin(list_months))
    .join( fb_active_users, on="user_id", how="left" )
    .where(F.col("number_of_comments")>0)
    .where(F.col("country").isNotNull())
    .groupBy("month", "country")
    .agg(
        F.sum("number_of_comments").alias("total_comments")
    )
    .withColumn( "comment_rank",
        F.row_number().over(
            Window.partitionBy("month").orderBy(F.col("total_comments").desc())
        )
    )
    .groupBy("country")
    .agg(
        F.max(
            F.when(
                F.col("month")==month1, F.col("comment_rank")
            ).otherwise(None)
        ).alias("rank_m1"),
        F.max(
            F.when(
                F.col("month")==month2, F.col("comment_rank")
            ).otherwise(None)
        ).alias("rank_m2")
    )
    .withColumn("rank_diff_m2_m1", F.col("rank_m2") - F.col("rank_m1"))
    #.where(F.col("rank_diff_m2_m1") > 0)
)
    
df_out = df_comments_per_month.orderBy("country")

# To validate your solution, convert your final pySpark df to a pandas df
pdf_out = df_out.toPandas()
