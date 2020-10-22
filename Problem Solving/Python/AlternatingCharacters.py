#You are given a string containing characters A and B only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

#Your task is to find the minimum number of required deletions.

#For example, given the string s=AABAAB, remove an A at positions 0 and 3 to make s=ABAB in 2 deletions.

#Function Description

#Complete the alternatingCharacters function in the editor below. It must return an integer representing the minimum number of deletions to make the alternating string.

#alternatingCharacters has the following parameter(s):
#s: a string

#Input Format

#The first line contains an integer q, the number of queries.
#The next q lines each contain a string s.

#Constraints
#1<=q<=10
#1<=|s|<=10^5
#Each string  will consist only of characters A and B

#Output Format
#For each query, print the minimum number of deletions required on a new line.

#Sample Input
#5
#AAAA
#BBBBB
#ABABABAB
#BABABA
#AAABBB

#Sample Output
#3
#4
#0
#0
#4

#!/bin/python3

import os

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    l=[]
    ct=0
    for ch in s:
        l.append(ch)
    a=[]
    a=l
    for i,tq in enumerate(l):
        for j in range(i+1, len(l)):
           if(l[i] == l[j]):
                a[j]=0
           else:
                break
    for i in a:
        if(i==0):
            ct+=1
    return ct
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
