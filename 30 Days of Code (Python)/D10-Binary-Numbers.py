'''
Objective
Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given a base-
integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in

's binary representation.

Input Format

A single integer,

.

Constraints

Output Format

Print a single base-
integer denoting the maximum number of consecutive 's in the binary representation of

.

Sample Input 1

5

Sample Output 1

1

Sample Input 2

13

Sample Output 2

2

Explanation

Sample Case 1:
The binary representation of
is , so the maximum number of consecutive 's is

.

Sample Case 2:
The binary representation of
is , so the maximum number of consecutive 's is .
'''

import math
import os
import random
import re
import sys


coun=0
if __name__ == '__main__':
    n = int(input())
b=str(bin(n))[2:].split('0')
print(len(max(b)))