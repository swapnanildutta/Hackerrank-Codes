"""
File: ExtraLongFactorials.py
Description: A solution for ExtraLongFactorials
Author: Nuttaphat Arunoprayoch
Date: 06-Oct-2020

Information
Link: https://www.hackerrank.com/challenges/extra-long-factorials
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
