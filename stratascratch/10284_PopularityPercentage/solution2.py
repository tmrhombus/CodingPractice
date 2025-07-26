# Import your libraries
import pyspark
import pyspark.sql.functions as F
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('sparkdf').getOrCreate()


nr_users = (
    facebook_friends
    .select(F.col("user1").alias("user"))
    .union(
        facebook_friends
        .select(F.col("user2").alias("user"))
    )
    .agg(
        F.countDistinct("user").alias("total")
    )
).toPandas()["total"][0]


pdf_fb_friends = facebook_friends.toPandas()

dict_friendlists = {}
for index, row in pdf_fb_friends.iterrows():
    #print(f"{index}, {row}")
    #print(f"{index}, {row['user1']}, {row['user2']}")
    if not row["user1"] in dict_friendlists:
        dict_friendlists[row["user1"]] = set()
    dict_friendlists[row["user1"]].add(row["user2"])

    if not row["user2"] in dict_friendlists:
        dict_friendlists[row["user2"]] = set()
    dict_friendlists[row["user2"]].add(row["user1"])    
    

dict_nr_friends = {}
for k, v in dict_friendlists.items():
    dict_nr_friends[k] = len(v)

data = [ (int(k), v) for k, v in dict_nr_friends.items() ]

#print(data)
df_friendcounts = spark.createDataFrame( data, ["user_id", "nr_friends"] )


df_popularity_pct = (
    df_friendcounts
    .withColumn("popularity_pct",
        100 * F.col("nr_friends")/nr_users
    )
    .select("user_id", "popularity_pct")
)

df_popularity_pct.orderBy("user_id").toPandas()
