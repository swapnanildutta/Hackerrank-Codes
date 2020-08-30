'''
Objective
Welcome to the last day! Today, we're discussing bitwise operations. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given set
. Find two integers, and (where ), from set such that the value of is the maximum possible and also less than a given integer, . In this case,

represents the bitwise AND operator.

Input Format

The first line contains an integer,
, the number of test cases.
Each of the subsequent lines defines a test case as space-separated integers, and

, respectively.

Constraints

Output Format

For each test case, print the maximum possible value of

on a new line.

Sample Input

3
5 2
8 5
2 2

Sample Output

1
4
0

Explanation

All possible values of and

are:

The maximum possible value of that is also is , so we print on a new line.
'''

import math
import os
import random
import re
import sys
from itertools import combinations

def maxbit(n, k):
    m = 0
    #for i,j in combinations(range(1,n+1), 2):
    for i in range(1, n + 1):
        for j in range(1, i):
            x = i & j
            if (m < x < k):
                m = x
                if (m == (k - 1)):
                    return m
    return m

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(maxbit(n, k))