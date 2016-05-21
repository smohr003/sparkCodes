''' This program multiply two matrix A and B. 
'''

from sys  import argv
from pyspark import SparkConf, SparkContext
from functools import partial
#method 1 
#sc = SparkContext("local", "App Name", pyFiles=['MyFile.py', 'lib.zip', 'app.egg'])



def getRowCol(filename,i): 

   return filename.map(lambda line: int(line.split(" ")[i])) \
             .reduce(lambda a,b : max(a,b))

# for each element: a, i,j,v produce this -> (i,k), (a,j,v) 
# this will repeat each element so we can send copies for the next step, which is reducer
def repeatElement(line, numRepeat, matName): 
	line = line.split(" ") 
	l = []	
	for k in range(1, numRepeat+1): 
	    keyEntry = (int(line[1]), k) 
	    valueEntry = [ matName,int(line[2]), int(line[3]) ]  
	    l.append( (keyEntry, valueEntry))
	return l
    
## this function will be used to compute the multiplicaiton of two vectors. 
# all elements of two vectors are send to one reducer. 
 
def multiply(allElements): 
	s = 0 
	#print(allElements)
	for a in allElements[1]: 
	   for b in allElements[1]: 
	    	if a[1] == b[1] and a[0] == 'a' and b[0]=='b': 
			s+= a[2]*b[2] 
	#print("sum is: ",s )
	return (allElements[0],s)


if __name__ == "__main__": 

	if len(argv) != 3:
	   print("Usage:  matMult <firstMatrixFileName> <secondMatrixFileName> ") 
	   exit(-1)
	aMat = argv[1]
	bMat = argv[2]


	conf = (SparkConf()
		 .setMaster("local")
		 .setAppName("My app")
		 .set("spark.executor.memory", "1g"))
	sc = SparkContext(conf = conf)

	
	text_file_a = sc.textFile(aMat)
	text_file_b = sc.textFile(bMat)
	rowA = getRowCol(text_file_a,1)
	colA = getRowCol(text_file_a,2)
	rowB = getRowCol(text_file_b,1)
	colB = getRowCol(text_file_b,2)
	
	#print("number of rows are ",rowA)
	 
	matCpart1 = text_file_a.flatMap(partial(repeatElement, numRepeat = colB, matName = 'a')) 

	matCpart2 = text_file_b.flatMap(partial(repeatElement, numRepeat = rowA, matName = 'b')) 


	#print(matCpart1.collect())

	matC = matCpart1 + matCpart2 

	#print(matC.collect())

	# due to limitations of spark, we don't have a traditional MR reducer, but we use the combination of groupby and map to emulate that behavior. 
	# for me look at Readme.me  	
	results = matC.groupByKey().map(multiply).collect()
	print(results)
	sc.parallelize(results).saveAsTextFile("cMatrix")

