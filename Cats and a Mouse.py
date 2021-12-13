
import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    for i in range(0,q):
        catch1= abs(z-x)
        catch2 = abs(z-y)
        if(catch1 > catch2):
            return 'Cat B'
        if(catch1 < catch2):
            return 'Cat A'
        if(catch1 == catch2):
            return 'Mouse C'
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()
        
        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
