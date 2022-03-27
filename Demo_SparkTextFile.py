#code: utf8

from pyspark import SparkConf, SparkContext

conf = SparkConf.setAppName("demo2").setMaster("local[*]")
sc = SparkContext(conf=conf)

sc.textFile("test1.txt,test2.txt")
print(sc.collect())
