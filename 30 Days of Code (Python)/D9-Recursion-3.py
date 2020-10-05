'''
Objective
Today, we're learning and practicing an algorithmic concept called Recursion. Check out the Tutorial tab for learning materials and an instructional video!

Recursive Method for Calculating Factorial

Task
Write a factorial function that takes a positive integer,
as a parameter and prints the result of (

factorial).

Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of

.

Input Format

A single integer,

(the argument to pass to factorial).

Constraints

    Your submission must contain a recursive function named factorial.

Output Format

Print a single integer denoting

.

Sample Input

3

Sample Output

6

Explanation

Consider the following steps:

From steps and , we can say ; then when we apply the value from to step , we get . Thus, we print as our answer.
'''

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()