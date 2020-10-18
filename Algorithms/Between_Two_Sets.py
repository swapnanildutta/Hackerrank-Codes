# https://www.hackerrank.com/challenges/between-two-sets/problem

#You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:

#The elements of the first array are all factors of the integer being considered
#The integer being considered is a factor of all elements of the second array
#These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.

#For example, given the arrays a=[2,6] and b=[24,36], there are two numbers between them: 6 and 12. 6%2=0, 6%6=0, 24%6=0 and 36%6=0 for the first value. Similarly, 12%2=0, 12%6=0 and 24%12=36%12=0 .

#Function Description

#Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.

#getTotalX has the following parameter(s):

#a: an array of integers
#b: an array of integers
#Input Format

#The first line contains two space-separated integers, n and m, the number of elements in array a and the number of elements in array b.
#The second line contains  distinct space-separated integers describing a[i] where 0<=i<n.
#The third line contains  distinct space-separated integers describing b[i] where 0<=j<m.

#Constraints
# 1<=n,m<=10
# 1<=a[i],b[j]<=100

#Output Format

#Print the number of integers that are considered to be between  and .

#Sample Input

#2 3
#2 4
#16 32 96
#Sample Output

#3
#Explanation

#2 and 4 divide evenly into 4, 8, 12 and 16.
#4, 8 and 16 divide evenly into 16, 32, 96.

#4, 8 and 16 are the only three numbers for which each element of a is a factor and each is a factor of all elements of b.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
