#!/bin/python3

#by Shanshan Wang
#https://www.hackerrank.com/cooleel

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    res = 'Yes'
    d = defaultdict(int) 
    for words in magazine: 
        d[words] += 1
    for w in note:
        if w not in d:
            res = "No"
        else:
            d[w] -= 1
            if d[w] < 0:
                res = "No"
    print(res)
   

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)