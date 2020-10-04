'''
Problem link - https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
@author - anurag kar
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#Complete the repeatedString function below.
def repeatedString(l, n):
  cnt = 0
  for i in range(1,n):
    if (l[i] == 'a'):
      cnt += 1
  return cnt

#for converting string to list
def Convert(st):
  li = list(st.split(" "))
  return li

#main function
if __name__ == '__main__':


    s = input()
    l = len(s)

    n = int(input())

    lst = []
    bst = []
    lst = Convert(s)
    for i in range(l,n):
      bst[i-l] = lst[i-l]

    c = lst + bst

    result = repeatedString(c, n)

    print(result)
