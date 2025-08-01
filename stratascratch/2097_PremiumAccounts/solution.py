
# Import your libraries
import pyspark
import pyspark.sql.functions as F

df_all_actives = (
    premium_accounts_by_day
    .where(F.col("final_price") > 0)
    .select("account_id", "entry_date")
    .withColumn("later_date", F.date_add("entry_date", 7))
)

df_active_later = (
    df_all_actives
    .withColumn("date_merge", F.col("later_date"))
    .join( (df_all_actives
            .withColumn("date_merge", F.col("entry_date")) 
            .withColumn("active_later", F.lit(1))
            .select("account_id", "date_merge", "active_later")
            )
        , on=["account_id", "date_merge"], how="inner"
    )
    .select("account_id", "entry_date", "active_later")
    .join(df_all_actives, on=["account_id", "entry_date"], how="right")
    .fillna(0)
)

df_active_by_date = (
    df_active_later
    .groupBy("entry_date")
    .agg(
        F.count("account_id").alias("nr_active_d1"),
        F.sum("active_later").alias("nr_active_later")
    )
)


df_active_by_date.orderBy("entry_date").limit(7).toPandas()


