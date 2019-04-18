#!/bin/bash


cd "$SPARK_HOME/jars"
path="[artifact]-[revision](-[classifier]).[ext]"
ivyjar="ivy-2.4.0.jar"
# 1. Download the latest ivy jar (currently it's v.2.4.0)
curl -L -O http://search.maven.org/remotecontent?filepath=org/apache/ivy/ivy/2.4.0/$ivyjar

# 2. Run ivy.jar to retrieve all dependencies
java -jar $ivyjar -dependency com.sparkjava spark-core 2.1 -retrieve $path  
java -jar $ivyjar -dependency ml.dmlc    xgboost4j-spark     0.80 -retrieve $path  # this needs spark 2.3+ ml.dmlc:xgboost4j-spark:0.80
java -jar $ivyjar -dependency com.esotericsoftware.reflectasm reflectasm   1.07 -retrieve $path # // NOTE: this is required for xgboost com.esotericsoftware.reflectasm:reflectasm:1.07
java -jar $ivyjar -dependency com.crealytics      spark-excel     0.9.18  -retrieve $path  #   version 0.10 currently has a bug in hdinsight :com.crealytics:spark-excel:0.9.18
java -jar $ivyjar -dependency com.typesafe     config     1.3.1  -retrieve $path 
java -jar $ivyjar -dependency com.typesafe.scala-logging      scala-logging     3.7.2  -retrieve $path 
java -jar $ivyjar -dependency org.scalatest     scalatest     2.2.0  -retrieve $path 
java -jar $ivyjar -dependency org.graphstream   gs-core   1.1.1  -retrieve $path 
java -jar $ivyjar -dependency guru.nidi     graphviz-java     0.2.3  -retrieve $path 
java -jar $ivyjar -dependency net.liftweb      lift-json     3.3.0  -retrieve $path 
java -jar $ivyjar -dependency com.typesafe.play      play-json     2.6.10  -retrieve $path 
java -jar $ivyjar -dependency org.apache.spark      spark-catalyst     2.3.1    -retrieve $path 
java -jar $ivyjar -dependency org.apache.spark      spark-tags     2.3.1  -retrieve $path 

