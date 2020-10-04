'''
Problem link - https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
@author - anurag kar
'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    up=0
    down=0
    valley=0
    net=0
    ref=0

    for x in s:
        if(x=='D'):
            down+=1
        else:
            up+=1

        net=up-down
        if(net>0):
            ref=1
        elif(net<0):
            ref=-1
        else:
            if(ref>0):
                pass
            else:
                valley+=1   

    return (valley)    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    if(n<2):
      sys.exit(1)

    s = input()
    for l in s:
      if(l!='D' and l!='U'):
        sys.exit(1)

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
