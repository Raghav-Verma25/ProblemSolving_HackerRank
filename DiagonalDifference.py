#!/bin/python3

import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    # Write your code here
    pri=0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if i==j:
                pri= pri + arr[i][j]
    #print(pri)

    sec=0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if ((i+j) == (len(arr)-1)):
                sec= sec+ arr[i][j]
    #print(sec)
    
    result = abs(pri - sec)    
    return result
        
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
