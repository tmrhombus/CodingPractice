
# Import your libraries
import pyspark
import pyspark.sql.functions as F

month_dec = "2020-12"
month_jan = "2021-01"
month_feb = "2021-02"

df_retention_ratio = (
    sf_events
    .withColumn("month_event", F.date_format("record_date", "yyyy-MM"))
    .withColumn("played_dec", 
        F.when(F.col("month_event") == month_dec, 1).otherwise(0)
    )
    .withColumn("played_jan", 
        F.when(F.col("month_event") == month_jan, 1).otherwise(0)
    )
    .withColumn("played_l8r", 
        F.when(F.col("month_event") >= month_feb, 1).otherwise(0)
    )
    .groupBy("user_id", "account_id")
    .agg(
        F.max(F.col("played_dec")).alias("played_dec"),
        F.max(F.col("played_jan")).alias("played_jan"),
        F.max(F.col("played_l8r")).alias("played_l8r")
    )
    .withColumn( "retained_dec",
        F.when(
                ( (F.col("played_dec")==1) &
                ( (F.col("played_jan") == 1) | (F.col("played_l8r") == 1 ) )  
                ), 1  
        ).otherwise(
            F.when(
                ( (F.col("played_dec")==1) & 
                ( (F.col("played_jan") == 0) & (F.col("played_l8r") == 0 ) )  
                ), 0
            ).otherwise(None)
        )
    )
    .withColumn( "retained_jan",
        F.when( 
            ( (F.col("played_jan")==1) & 
              ( (F.col("played_l8r") == 1 ) )  
            ), 1  
        ).otherwise(
            F.when(
                ( (F.col("played_jan")==1) & 
                ( (F.col("played_l8r") == 0 ) )  
                ), 0
            ).otherwise(None)
        )
    )    
    .groupBy("account_id")
    .agg(
        F.sum("played_dec").alias("tot_dec"),
        F.sum("retained_dec").alias("ret_dec"),
        F.sum("played_jan").alias("tot_jan"),
        F.sum("retained_jan").alias("ret_jan"),
    )
    .withColumn("frac_ret_dec",
        F.when(F.col("tot_dec")>0, F.col("ret_dec")/F.col("tot_dec")).otherwise(0)
    )
    .withColumn("frac_ret_jan",
        F.when(F.col("tot_jan") > 0, F.col("ret_jan")/F.col("tot_jan")).otherwise(0)
    )
    .withColumn("ret_ratio_jan_dec",
        F.when(F.col("frac_ret_dec") > 0, F.col("frac_ret_jan")/F.col("frac_ret_dec") ).otherwise(0)
    )

)

df_retention_ratio.select("account_id", "ret_ratio_jan_dec").toPandas()
