
# Import your libraries
import pyspark
import pyspark.sql.functions as F

df_bigwinner = (
    oscar_nominees
    .where(F.col("winner")==True)
    .groupBy("nominee")
    .agg(
        F.count("movie").alias("nr_wins")    
    )
    .orderBy(F.col("nr_wins").desc(), F.col("nominee"))
    .limit(1)
    .join(
        nominee_information.withColumnRenamed("name", "nominee"), 
        on="nominee",
        how="inner"
    )
    .select("top_genre")
)
df_bigwinner.toPandas()


