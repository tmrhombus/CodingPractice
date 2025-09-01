
# Import your libraries
import pyspark
import pyspark.sql.functions as F
from pyspark.sql.window import Window

df_streaks = (
    sf_events
    .select("user_id", "record_date")
    .distinct()
    .withColumn("day_nr", 
        F.row_number().over(
            Window.partitionBy("user_id").orderBy(F.col("record_date"))
        )
    )
    .withColumn("streak_nr",
        F.date_sub(F.col("record_date"),  F.col("day_nr"))
    )
    .groupBy("user_id", "streak_nr")
    .agg(
        F.count("record_date").alias("streak_length")    
    )
    .where(F.col("streak_length") >= 3 )
    .select("user_id")
    .distinct()
)

df_out = df_streaks.toPandas()


