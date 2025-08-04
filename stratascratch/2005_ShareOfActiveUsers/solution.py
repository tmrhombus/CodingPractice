
# Import your libraries
import pyspark
import pyspark.sql.functions as F

nr_users = (
    fb_active_users
    .select("user_id")
    .distinct()
).count()

nr_us_open_users = (
    fb_active_users
    .where(F.col("status")=="open")
    .where(F.col("country")=="USA")
    .select("user_id")
    .distinct()
).count()

out = 100 * nr_us_open_users / nr_users


