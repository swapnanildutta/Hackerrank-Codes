'''
ALMOST SORTED

Given an array of integers, determine whether the array can be sorted in ascending order using only one of the following operations one time.

1. Swap two elements.
2. Reverse one sub-segment.
Determine whether one, both or neither of the operations will complete the task. If both work, choose swap. For instance, given an array [2,3,4,5] either swap the 4 and 5, or reverse them to sort the array. Choose swap. The Output Format section below details requirements.

Function Description

Complete the almostSorted function in the editor below. It should print the results and return nothing.

almostSorted has the following parameter(s):

* arr: an array of integers

Input Format

The first line contains a single integer n, the size of arr.
The next line contains n space-separated integers arr[i] where 1<=i<=n.

Constraints

2<=n<=100000
0<=arr[i]<=1000000
All arr[i] are distinct

Output Format

1. If the array is already sorted, output yes on the first line. You do not need to output anything else.

2. If you can sort this array using one single operation (from the two permitted operations) then output yes on the first line and then:

    a. If elements can be swapped, d[l] and d[r], output swap l r in the second line. l and r are the indices of the elements to be swapped, assuming that the array is indexed from 1 to n.

    b. Otherwise, when reversing the segment d[l...r], output reverse l r in the second line. l and r are the indices of the first and last elements of the subsequence to be reversed, assuming that the array is indexed from 1 to n.

    d[l...r] represents the sub-sequence of the array, beginning at index l and ending at index r, both inclusive.

If an array can be sorted by either swapping or reversing, choose swap.

3. If you cannot sort the array either way, output no on the first line.

Sample Input 1

2  
4 2  
Sample Output 1

yes  
swap 1 2
Explanation 1

You can either swap(1, 2) or reverse(1, 2). You prefer swap.

Sample Input 2

3
3 1 2
Sample Output 2

no
Explanation 2

It is impossible to sort by one single operation.

Sample Input 3

6
1 5 4 3 2 6
Sample Output 3

yes
reverse 2 5
Explanation 3

You can reverse the sub-array d[2...5] = "5 4 3 2", then the array becomes sorted.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):
    peaks=[]
    valleys=[]
    arr.insert(0,0)
    arr.append(1000001)
    for i in range(1, len(arr)-1):
        if arr[i]<arr[i-1] and arr[i]<arr[i+1]:
            valleys.append(i)
        elif arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            peaks.append(i)
    if len(valleys) == 0 or len(peaks) == 0:
        print('yes')
    elif len(valleys) > 2 or len(peaks) > 2:
        print('no')
    elif len(valleys) == 1 and len(peaks) == 1:
        v = valleys[0]
        p = peaks[0]
        if arr[v]>arr[p-1] and arr[p]<arr[v+1]:
            print('yes')
            if v-p==1:
                print('swap', p, v)
            else:
                print('reverse', p, v)
        else:
            print('no')
    elif len(valleys) == 2 and len(peaks) == 2:
        p1 = peaks[0]
        p2 = peaks[1]
        v1 = valleys[0]
        v2 = valleys[1]
        if arr[v2]>arr[p1-1] and arr[v2]<arr[p1+1] and arr[p1]<arr[v2+1] and arr[p1]>arr[p2] and v1-p1==1 and v2-p2==1:
            print('yes')
            print('swap', p1, v2)
        else:
            print('no')


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)