# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:15:37 2020

@author: Tanmoyee
"""

''' A left rotation operation on an array of size n shifts each of the array's elements 1 unit to the left. Given an integer, d, rotate the array that many steps left and return the result.

Example

d=2
arr=[1,2,3,4,5]
after 2 rotations, arr'=[3,4,5,1,2]
'''






#!/bin/python3

import math
import os
import random
import re
import sys

def left_rotate(a,d):
    l=a[d:] + a[:d]
    print(" ".join(list(map(str,l))))

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    result=left_rotate(a,d)
    
