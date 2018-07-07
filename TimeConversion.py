#!/bin/python3

#by Shanshan Wang
#https://www.hackerrank.com/cooleel

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def timeConversion(s):
    s1 = int(s[:2])
    f = 0
    if s[-2] =='P':
        if s1 >0 and s1 <12:
            f = s1 +12
        elif s1 ==12:
            f = 12
    elif s[-2] =='A':
        if s1 >0 and s1 <12:
            f = s1
        elif s1 ==12:
            f = 0
    f1 = str(f).zfill(2)
    return(f1+s[2:-2])

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()