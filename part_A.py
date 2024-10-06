
import math

x = [1,2,3,4,5]

def std_loops(x):
    
    sumx = 0
    for num in x:
        sumx += num
    mean = sumx / len(x)

    sumSqD = 0 
    for num in x:
        sumSqD += (num - mean)**2
    var = sumSqD / len(x)

    stdDev = math.sqrt(var)
    print(stdDev)
    


def std_builtin(x):
   
   for num in x:
        mean = sum(x)/len(x)
        sqDiff = []
        sqDiff.append((num - mean)**2)
        var = sum(sqDiff)/len(x)
        stdDev = math.sqrt(var)
    print(stdDev)
   

import NumPy

def std_numpy(x):

    print(NumPy.std(x)) 
