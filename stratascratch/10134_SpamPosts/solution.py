# Import your libraries
import pyspark
import pyspark.sql.functions as F


df_post_spam = (
    facebook_posts
    .withColumn("is_spam",
        F.when(F.col("post_keywords").contains("spam"), 1).otherwise(0)
    )
    .groupBy("post_id")
    .agg(
        F.max("is_spam").alias("is_spam"),
        F.mode("post_date").alias("post_date")
    )
    .select("post_id", "post_date", "is_spam")
)


df_spamfrac = (
    df_post_spam
    .join( facebook_post_views, on="post_id", how="inner" )
    .groupBy("post_date")
    .agg(
        F.count("post_id").alias("nr_views"),
        F.sum("is_spam").alias("nr_spam_views")
    )
    .withColumn("spam_frac", 100 * F.col("nr_spam_views")/F.col("nr_views"))
)

df_spamfrac.select("post_date", "spam_frac").orderBy("post_date").toPandas()
