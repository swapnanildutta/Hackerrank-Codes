#!/bin/python3

import math
import os
import random
import re
import sys


def countingValleys(n, s):    
    lvl = 0
    vly = 0
    for i in s:
        if i == 'U':
            lvl += 1
        else:
            lvl -= 1
        if i == 'U' and lvl == 0:
            vly += 1
    return vly
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
