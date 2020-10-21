'''
Given a sequence of integers , a triplet

is beautiful if:

Given an increasing sequenc of integers and the value of

, count the number of beautiful triplets in the sequence.

For example, the sequence
and . There are three beautiful triplets, by index: . To test the first triplet, and

.

Function Description

Complete the beautifulTriplets function in the editor below. It must return an integer that represents the number of beautiful triplets in the sequence.

beautifulTriplets has the following parameters:

    d: an integer
    arr: an array of integers, sorted ascending

Input Format

The first line contains
space-separated integers and , the length of the sequence and the beautiful difference.
The second line contains space-separated integers

.

Constraints

Output Format

Print a single line denoting the number of beautiful triplets in the sequence.

Sample Input

7 3
1 2 4 5 7 8 10

Sample Output

3

Explanation

The input sequence is
, and our beautiful difference . There are many possible triplets , but our only beautiful triplets are , and

by value not index. Please see the equations below:




Recall that a beautiful triplet satisfies the following equivalence relation:
where . 
'''

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    #l=len(arr)
    trip=0
    for i in arr:
        if (i+d) in arr and (i+2*d) in arr:
            trip+=1
    return trip


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()