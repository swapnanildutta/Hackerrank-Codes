'''There is a collection of input strings and a collection of query strings. 
For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.
strings=['abc','ab','ab']
queries=['ab','abc','cc']
The output will be res=[2,1,0]

Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in strings.

matchingStrings has the following parameters:

-string strings[n] - an array of strings to search
-string queries[q] - an array of query strings
Returns

int[q]: an array of results for each query
Sample Input
4
aba
baba
aba
xzxb
3
aba
xzxb
ab
------------
Output
2
0
1





'''



import math
import os
import random
import re
import sys


# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    reslis=[]
   
    for x in queries:
        count=0
        if x in strings:
            count=strings.count(x)
        reslis.append(count)
    return reslis        



if __name__ == '__main__':
    

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)
    for re in res:
        print(re)
