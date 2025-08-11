
# Import your libraries
import pyspark
import pyspark.sql.functions as F
from pyspark.sql.window import Window

# Start writing code
df_out = (
 players_results
 .withColumn( "match_nr",  
    F.row_number().over(Window.partitionBy("player_id").orderBy("match_date"))
 )
 .where(F.col("match_result")=="W")
 .withColumn("win_nr",
    F.row_number().over(Window.partitionBy("player_id").orderBy("match_nr"))
 )
 .withColumn("match_win_gap", F.col("match_nr") - F.col("win_nr"))
 .groupBy("player_id","match_win_gap")
 .agg(
    F.count("match_nr").alias("streak_length")
 )
 .groupBy("player_id")
 .agg(
    F.max("streak_length").alias("longest_streak")    
 )
 .withColumn("streak_rank",
    F.dense_rank().over(
        Window.orderBy(F.col("longest_streak").desc())
    )
 )
 .where(F.col("streak_rank")==1)
)


df_out.select("player_id", "longest_streak").toPandas()


