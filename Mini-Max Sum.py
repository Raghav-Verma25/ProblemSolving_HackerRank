
import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    # Write your code here
    #FOR MAX
    
    max_num = max(arr)
    arr.remove(max_num)
    sumofmax = sum(arr)
    # FOR MIN
    
    arr.append(max_num)
    min_num = min(arr)
    arr.remove(min_num)
    sumofmin = sum(arr)
    
    print(sumofmax , sumofmin)
    
    
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
