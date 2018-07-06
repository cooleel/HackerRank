#!/bin/python3

#by Shanshan Wang
#https://www.hackerrank.com/cooleel

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    k = 0
    for i in a:
        if b.find(i) != -1:
            b = b.replace(i,'',1)
            k +=1
    count = len(a)+len(b) - k
    return count
    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()