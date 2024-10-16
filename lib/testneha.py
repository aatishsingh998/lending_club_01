print("how to create dataframe using python list")
from pyspark.sql.types import *

data=[1,2,3,4,5]

df = spark.createDataFrame([(i,) for i in data]).toDF("id")
#
# df.show()
#
# data=[(1,),(2,),(3,),(4,),(5,)]
#
# df = spark.createDataFrame(data)
#
# df.show()
