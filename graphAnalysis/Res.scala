// This program simulate the construction of a graph using GraphX. This version simulates removing some edges and measures the max degree of
// graph before and after removing 
// Author:   Shahram Mohrehkesh (smohr003@odu.edu)
// Created:  09/17/2016
//
// Copyright (C) 2016 
// For license information, see LICENSE.txt
 

import org.apache.spark._
 
import org.apache.spark.graphx._
import org.apache.spark.rdd.RDD

 
object Res  {
   def main(args: Array[String]) {
  
	val graphFile = args(0) 
	val removeEdgesFile = args(1) 
	 
	//
    	val conf = new SparkConf().setAppName("Graph Application")
 

	// Assume the SparkContext has already been constructed
	//val sc: SparkContext
	 	
	val sc = new SparkContext(conf)

	val outfile = "ResOut"

 
	 
	 
	// Build the initial Graph
	val graph = GraphLoader.edgeListFile(sc, graphFile)  

	 
	graph.triplets.map(
	    triplet => triplet.srcId + " is the " + "neighbor"+ " of " + triplet.dstId
	  ).collect.foreach(println(_))
 
	val maxDegrees: (VertexId, Int)   = graph.degrees.reduce(max) 
	println("Initial max degree is")
	println(maxDegrees)
 
	sc.parallelize(Array(maxDegrees)).saveAsTextFile(outfile)
 	


 
	val ccGraph = graph.connectedComponents()
	println("Initial Connected graph is: ")
 	ccGraph.vertices.collect.foreach(println(_))
 

 	// remove edges 

	// removes all edges that their vertices in the list 
	val removeList = List(1,2,3)
	val partialGraph = Graph(graph.vertices, graph.edges.filter(e => !(removeList.contains(e.srcId)) &&   !(removeList.contains(e.dstId)) ) )  

	

	val maxDegreesPartial: (VertexId, Int)   = partialGraph.degrees.reduce(max) 
	println("Final max degree is")
	println(maxDegreesPartial)
	sc.parallelize(Array(maxDegreesPartial)).saveAsTextFile(outfile)
 
	val ccGraphPartial = graph.connectedComponents()
	println("Final Connected graph is: ")
	ccGraphPartial.vertices.collect.foreach(println(_))
 
	 
	
     } 
     
     def max(a: (VertexId, Int), b: (VertexId, Int)): (VertexId, Int) = {
 	 if (a._2 > b._2) a else b
     }

}
