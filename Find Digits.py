
import math
import os
import random
import re
import sys



def findDigits(n):
    # Write your code here
    n=abs(n)
    for k in range(0,t):
        count=0
        c=str(n)
        lst=list(c)
        lst2=[]
        for i in lst:
            lst2.append(int(i))
        for j in lst2:
            if j>0:
                if n%j==0:
                    count=count+1
        return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
