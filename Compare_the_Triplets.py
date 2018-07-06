#!/bin/python3

#by Shanshan Wang
#https://www.hackerrank.com/cooleel

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(a, b):
    i = 0
    j = 0
    n = len(a)

    for x in range(n):
        if a[x] > b[x]:
            i += 1
        elif a[x] < b[x]:
            j += 1
        else:
            pass
    scoure = [i, j]
    return scoure

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = solve(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()