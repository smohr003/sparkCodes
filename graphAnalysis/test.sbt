name := "Graph Project"

version := "1.3.0"

scalaVersion := "2.11.7"

libraryDependencies += "org.apache.spark" %% "spark-core" % "2.0.0"

libraryDependencies += "org.apache.spark" % "spark-streaming_2.11" % "2.0.0"

libraryDependencies +=  "org.apache.spark"  %% "spark-graphx" % "1.4.0"  % "provided"
