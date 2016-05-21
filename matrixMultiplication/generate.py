import random 
from sys import argv

if __name__ == "__main__": 

  if len(argv) < 4:
    print("correct usage: [outputfilename] [#row] [#col] [matName]") 
    exit(1)

  matName = argv[4]
  with open(argv[1], "w") as f :

     for i in range(1, int(argv[2])+1): 
        for j in range(1, int(argv[3])+1):  

           f.write(matName + " "+ str(i)+ " "+ str(j)+  " 1\n")
           
