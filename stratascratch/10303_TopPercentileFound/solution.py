
# Import your libraries
import pyspark
import pyspark.sql.functions as F
from pyspark.sql.window import Window

df_top_frauds = (
    fraud_score
    .withColumn("fraud_pct", 
        F.percent_rank().over(
            Window.partitionBy("state").orderBy(F.col("fraud_score"))
        )
    )
    .where(F.col("fraud_pct") >= 0.95)
    .select("policy_num", "state", "claim_cost", "fraud_score")
).toPandas()



