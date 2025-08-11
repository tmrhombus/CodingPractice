
# Import your libraries
import pyspark
import pyspark.sql.functions as F
from pyspark.sql.window import Window

startdate = "2022-08-10"

df_streaks = (
    user_streaks
    .withColumn( "dt_visit", F.date_format(F.col("date_visited"), "yyyy-MM-dd") )
    .where(F.col("dt_visit")<=startdate)
    .distinct()
    #.wtihColumn("dt_next", F.date_add(F.col("dt_visit"), 1 ), 
    .withColumn( "day_nr", 
        F.row_number().over(
            Window.partitionBy("user_id").orderBy("dt_visit")
        ) 
    )
    .withColumn("ref_date", F.date_add("dt_visit", -1 * F.col("day_nr")))
    .groupBy( "user_id", "ref_date" )
    .agg(F.count("user_id").alias("counts_per_refdate"))
    .groupBy("user_id")
    .agg(F.max("counts_per_refdate").alias("longest_streak"))
)

pdf_out = (
    df_streaks
    .orderBy(F.col("longest_streak").desc())
    .limit(3)
).toPandas()
