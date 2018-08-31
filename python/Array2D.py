# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 10:46:18 2018
D2Array-DS
sum of all hourglasses inside a NXN array
3-1-3 hourglasses

@author: Shanshan
"""

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum = []
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            sum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])

    return max((sum))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()