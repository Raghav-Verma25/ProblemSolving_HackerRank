
import math
import os
import random
import re
import sys


def camelcase(s):
    word=0
    j=0
    for i in range(0,len(s)):
        if (s[j]>=chr(65) and s[j]<=chr(90)):
            word = word + 1
        j=j+1
    if (s[0]>=chr(97) and s[0]<=chr(122)):
        word =word + 1
    return word
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
