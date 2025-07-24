# Import your libraries
import pyspark
import pyspark.sql.functions as F
from pyspark.sql.window import Window

month1 = "2019 12"
month2 = "2020 01"
list_months = [month1, month2]    
    
    
# fb_comments_count user_id, created_at, number_of_comments
# fb_active_users user_id, name, status, country
    
df_countries = (
    fb_active_users
    .select("country")
    .distinct()
)    

df_months = (
    fb_comments_count
    .withColumn("month", F.date_format("created_at", "yyyy MM"))
    .where(F.col("month").isin(list_months))
    .select("month")
    .distinct()
)

df_countries_months = (
    df_countries.crossJoin(df_months)
)


df_raw_rank_per_month = (
    fb_comments_count
    .withColumn("month", F.date_format("created_at", "yyyy MM")) 
    .where(F.col("month").isin(list_months))
    .join(fb_active_users.select("user_id","country"), on="user_id", how="left")
    .groupBy("month", "country")
    .agg(
        F.sum("number_of_comments").alias("monthly_comment_count")    
    )
    .where(F.col("country").isNotNull())
    .join(df_countries_months, on=["country", "month"], how="right")
    .fillna(0, subset=["monthly_comment_count"])
    .withColumn("monthly_rank",
        #F.row_number().over( 
        F.dense_rank().over( 
            Window.partitionBy("month").orderBy(
                F.col("monthly_comment_count").desc()
            )
        )
    )
)

df_mod_rank_per_month = (
    df_raw_rank_per_month
    .groupBy("month", "monthly_comment_count")
    .agg(
        F.min("monthly_rank").alias("mod_monthly_rank")    
    )
)

df_rank_variation = (
    df_raw_rank_per_month
    .join(df_mod_rank_per_month, on=["month", "monthly_comment_count"], how="inner")
    .groupBy("country")
    .agg(
        F.max(
            F.when(F.col("month") == month2, F.col("mod_monthly_rank")).otherwise(None)
        ).alias("rank_m2"),
        F.max(
            F.when(F.col("month") == month1, F.col("mod_monthly_rank")).otherwise(None)
        ).alias("rank_m1"),
    )
    .withColumn("rank_diff", F.col("rank_m2")-F.col("rank_m1"))
    .where(F.col("rank_diff") < 0)
)

df_out = df_rank_variation

# To validate your solution, convert your final pySpark df to a pandas df
pdf_out = df_out.toPandas()
