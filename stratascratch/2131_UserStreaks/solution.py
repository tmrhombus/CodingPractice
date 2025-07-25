# Import your libraries
import pyspark
import pyspark.sql.functions as F
from pyspark.sql.window import Window
import numpy as np
import pandas as pd

from pyspark.sql import SparkSession

# creating sparksession and giving 
# an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

startdate = "2022-08-10"

# Start writing code
df_playdates = (
    user_streaks
    .select("user_id", "date_visited")
    .distinct()
    .withColumn("dt", F.date_format("date_visited", "yyyy-MM-dd"))
    .where(F.col("dt") <= startdate)
    .withColumn("dt_tomorrow", F.date_add(F.col("dt"), 1))
    .withColumn("next_play", 
        F.lead(F.col("dt"), 1).over(
            Window.partitionBy(F.col("user_id")).orderBy(F.col("dt"))
        )
    )
    .withColumn("played_tomorrow",
        F.when(F.col("dt_tomorrow")==F.col("next_play"), 1).otherwise(0)
    )
)


pdf_playdates = df_playdates.orderBy("user_id", "dt").toPandas()

#print(pdf_playdates)

pdf_ids = user_streaks.select("user_id").distinct().toPandas()

dict_id_playtomorrow = {}
for index, idrow in pdf_ids.iterrows():
    #print(f"{type(index)} {type(theid[0])}")
    #print(f"{index} {theid[0]}")
    theid = idrow[0]
    
    #print(pdf_playdates[ pdf_playdates["user_id"]==theid ]["played_tomorrow"])
    
    dict_id_playtomorrow[theid] = pdf_playdates[ pdf_playdates["user_id"]==theid ]["played_tomorrow"].to_numpy()
    
    
def find_longest_streak(arr_in):
    ls = 1 ## longest streak
    ts = 1 ## this streak
    for i in arr_in:
        if i == 1:
            ts += 1 
        else:
            if ts > ls: 
                ls = ts
            ts = 1
            
    return ls
    
dict_id_ls = {}
for theid in dict_id_playtomorrow.keys():
    thearr = dict_id_playtomorrow[theid]
    #print(f"{theid} :: {thearr}")
    dict_id_ls[theid] = find_longest_streak(thearr)
 
 
#print(dict_id_ls) 

data_tuples = [(k, v) for k, v in dict_id_ls.items()]

# Create DataFrame
df_id_ls = spark.createDataFrame(data_tuples, ['user_id', 'streak_length'])
 
df_top3 = (
    df_id_ls
    .withColumn("rank", 
        F.dense_rank().over(Window.orderBy(F.col("streak_length").desc()))
    )
    .where(F.col("rank")<=3)
)
 
 
pdf_out = df_top3.orderBy("rank").select("user_id","streak_length").toPandas()

