
# Import your libraries
import pyspark
import pyspark.sql.functions as F

thedate = "2020-01-10"

df_ratio = (
    fb_account_status
    .withColumn("dt", F.date_format("status_date", "yyyy-MM-dd"))
    .where(F.col("dt")==thedate)
    .agg(
        F.count("acc_id").alias("nr_accounts"),
        F.sum(
            F.when( 
                ( F.col("status")=="closed" )    
            , 1).otherwise(0)    
        ).alias("nr_closed")
    )    
    .withColumn("frac_closed", F.col("nr_closed")/F.col("nr_accounts"))
)


df_ratio.select("frac_closed").toPandas()
