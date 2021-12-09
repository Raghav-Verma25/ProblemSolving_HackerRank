
import math
import os
import random
import re
import sys
def compareTriplets(a, b):
    # Write your code here
    alice=0
    bob=0
    z=0
    for i in range(0,len(a)):
            if a[i]==b[i]:
                z=z+1
            if a[i]>b[i]:
                alice = alice + 1
            if b[i]>a[i]:
                bob = bob + 1
    return alice , bob

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
