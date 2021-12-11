import math
import os
import random
import re
import sys

def plusMinus(arr):
    positive = 0
    negative=0
    zero = 0
    for i in arr:
        
        if i>0 :
            positive = positive + 1

        if i<0:
            negative = negative + 1
        
        if i==0 :
            zero = zero + 1
        
  

    p_ratio = positive/ len(arr)
    n_ratio = negative / len(arr)
    z_ratio = zero / len(arr)
    print(format(p_ratio , '.6f'))
    print(format(n_ratio , '.6f'))
    print(format(z_ratio , '.6f'))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
