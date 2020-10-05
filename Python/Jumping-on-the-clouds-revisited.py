#!/bin/python3

import math
import os
import random
import re
import sys

# c = list of clouds
def jumpingOnClouds(c, k):
    energy = 100
    i = 0
    while i in range(0, len(c)):
        if c[i] == 0:
            energy -= 1
        elif c[i] == 1:
            energy -= 3
        
        if i + k > len(c):
            i = (i + k) % n
        else:
            i += k
    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split() 
    n = int(nk[0]) # nr of clouds
    k = int(nk[1]) # jump distance

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')
    fptr.close()
