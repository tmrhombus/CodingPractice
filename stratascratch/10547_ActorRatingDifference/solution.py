# Import your libraries
import pyspark
import pyspark.sql.functions as F
from pyspark.sql.window import Window


df_nfilms = (
    actor_rating_shift
    .withColumn("nfilm",
        F.row_number().over(
            Window.partitionBy("actor_name").orderBy(F.col("release_date").desc())  
        )
    )
)

df_avg_rating = (
    actor_rating_shift
    .join(df_nfilms.select("nfilm", "actor_name", "film_title"),
        on=["actor_name", "film_title"], how="inner"
    )
    .where(F.col("nfilm") != 1)
    .groupBy("actor_name")
    .agg(
        F.avg("film_rating").alias("avg_rating")    
    )
)

df_out = (
    df_nfilms
    .where(F.col("nfilm") == 1)
    .withColumnRenamed("film_rating", "most_recent_rating")
    .join( df_avg_rating, on="actor_name", how="left" )
    .withColumn( "avg_lifetime_rating", 
        F.when(
        F.col("avg_rating").isNotNull()
        , F.col("avg_rating")    
        ).otherwise(F.col("most_recent_rating"))
    )
    .withColumn("rating_difference",
        F.col("most_recent_rating") - F.col("avg_lifetime_rating")
    )
)

cols_out = ["actor_name", "most_recent_rating",  "avg_lifetime_rating", "rating_difference"]
df_out.select(cols_out).toPandas()

