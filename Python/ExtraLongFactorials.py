"""
File: ExtraLongFactorials.py
Description: A solution for ExtraLongFactorials
Author: Nuttaphat Arunoprayoch
Date: 06-Oct-2020

# Information
Link: https://www.hackerrank.com/challenges/extra-long-factorials

The factorial of the integer , written , is defined as:
n! = n * (n-1) * (n-2) * .... 1
Calculate and print the factorial of a given integer.
For example, if n=30, we calculate 30*29*28*....*1

# Function Description
Complete the extraLongFactorials function in the editor below. It should print the result and return.
extraLongFactorials has the following parameter(s):
    * n -> int

Note: Factorials of  can't be stored even in a  long long variable. Big integers must be used for such calculations.
Languages like Java, Python, Ruby etc. can handle big integers, but we need to write additional code in C/C++ to handle huge values.
We recommend solving this challenge using BigIntegers.

# Input Format
Input consists of a single integer 

# Constraints
1 <= n <= 100

# Output Format
Print the factorial of n.

# Sample Input
25

# Sample Output
15511210043330985984000000
"""
# Import libraries
import math
import os
import random
import re
import sys
from functools import reduce


# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    all_nums = [i for i in range(1, n+1)]
    res = reduce(lambda x,y: x*y, all_nums)
    print(res)
    return res


if __name__ == '__main__':
    n = int(input())
    extraLongFactorials(n)
