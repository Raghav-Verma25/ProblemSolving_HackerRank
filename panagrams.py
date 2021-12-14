import math
import os
import random
import re
import sys

def pangrams(s):
    # Write your code here
    d=s.lower()
    s1=d.replace(' ','')
    s2=set(s1)
    if len(s2)==26:
        return 'pangram'
    else:
        return 'not pangram'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
