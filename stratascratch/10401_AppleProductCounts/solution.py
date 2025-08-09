# Import your libraries
import pyspark
import pyspark.sql.functions as F

# Start writing code

mac_devices = [
    "macbook pro",
    "iphone 5s",
    "ipad air"
]

df_all_users = (
    playbook_events
    .select("user_id")
    .distinct()
)

df_mac_users = (
    playbook_events
    .where(F.col("device").isin(mac_devices))
    .select("user_id")
    .distinct()
)

df_mac_language_counts = (
    df_mac_users
    .join(playbook_users, on="user_id", how="left")
    .groupBy("language")
    .agg(F.count("user_id").alias("nr_mac_users"))
)

df_all_language_counts = (
    df_all_users
    .join(playbook_users, on="user_id", how="left")
    .groupBy("language")
    .agg(F.count("user_id").alias("nr_all_users"))
)

df_out = (
    df_all_language_counts
    .join(df_mac_language_counts, on="language", how="left")
    .fillna(0)
    .select("language", "nr_mac_users", "nr_all_users")
)

# To validate your solution, convert your final pySpark df to a pandas df
df_out.orderBy(F.col("nr_all_users").desc()).toPandas()
