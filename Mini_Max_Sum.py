#!/bin/python3

#by Shanshan Wang
#https://www.hackerrank.com/cooleel

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_ = sum(arr)-max(arr)
    max_ = sum(arr)-min(arr)
    print(min_, max_)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)