#code: utf8
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("de").setMaster("local[*]")
sc = SparkContext(conf=conf)

rdd = sc.parallelize(range(1,11))
print(rdd.collect())