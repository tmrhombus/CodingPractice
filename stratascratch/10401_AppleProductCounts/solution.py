
# Import your libraries
import pyspark
import pyspark.sql.functions as F

# Start writing code

valid_devices = [
    "macbook pro",
    "iphone 5s",
    "ipad air"
]

df_valid_users = (
    playbook_events
    .where(F.col("device").isin(valid_devices))
    .select("user_id")
    .distinct()
)

df_user_language_counts = (
    df_valid_users
    .join(playbook_users, on="user_id", how="left")
    .select("user_id", "language")
    .groupBy("language")
    .agg(
        F.count("user_id").alias("nr_valid_users")
    )
)

df_all_language_counts = (
    playbook_users
    .groupBy("language")
    .agg(
        F.count("user_id").alias("nr_total_users")    
    )
)

df_out = (
    df_user_language_counts
    .join(df_all_language_counts, on="language", how="right")
    .fillna(0)
    .select("language", "nr_valid_users", "nr_total_users")
)


# To validate your solution, convert your final pySpark df to a pandas df
df_out.orderBy(F.col("nr_total_users").desc()).toPandas()
