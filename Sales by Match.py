
import math
import os
import random
import re
import sys


def sockMerchant(n, ar):

    count=0
    s=set(ar)
    for i in s:
        x=ar.count(i)
        y=x//2
        count=count+y
    return count

    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
