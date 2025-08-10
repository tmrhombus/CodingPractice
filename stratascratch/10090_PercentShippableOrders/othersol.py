
# Import your libraries
import pyspark
import pyspark.sql.functions as F

df_customer_status = (
    customers
    .withColumn("isShippable",
        F.when(
            ((F.col("address").isNotNull()) & (F.col("city").isNotNull())), 
        1).otherwise(0)
    )
    .select(
        F.col("id").alias("cust_id"),
        F.col("isShippable")
    )
)

df_valid_order_pct = (
    orders
    .join(df_customer_status, on="cust_id", how="left")
    .fillna(0)
    .agg(
        F.sum(
         F.when(
          F.col("isShippable")==1
         ,1).otherwise(0)
        ).alias("nr_shippable_orders"),
        F.count("id").alias("nr_all_orders")
    )
    .withColumn("pct_shippable_orders",
        F.floor(100 * F.col("nr_shippable_orders") / F.col("nr_all_orders")
    )    
    )
    .select("pct_shippable_orders")
)

df_valid_order_pct.toPandas()
