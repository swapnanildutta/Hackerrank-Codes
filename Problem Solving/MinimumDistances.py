'''
We define the distance between two array values as the number of indices between the two values. Given , find the minimum distance between any pair of equal elements in the array. If no such value exists, print

.

For example, if
, there are two matching pairs of values: . The indices of the 's are and , so their distance is . The indices of the 's are and , so their distance is

.

Function Description

Complete the minimumDistances function in the editor below. It should return the minimum distance between any two matching elements.

minimumDistances has the following parameter(s):

    a: an array of integers

Input Format

The first line contains an integer
, the size of array .
The second line contains space-separated integers

.

Constraints

Output Format

Print a single integer denoting the minimum
in . If no such value exists, print

.

Sample Input

6
7 1 3 4 1 7

Sample Output

3

Explanation
Here, we have two options:

and are both , so
.
and are both , so

    .

The answer is
.
'''

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    dis=2000
    for l in range(len(a)):
        try:
            u=a.index(a[l],l+1,len(a)) 
            dis=min(dis,u-l)
        except:
            pass
        
    if dis==2000:
        return -1
    return dis

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()