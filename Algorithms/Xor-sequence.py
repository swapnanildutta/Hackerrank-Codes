# https://www.hackerrank.com/challenges/xor-se/problem
# An array, A, is defined as follows:
# A[0] = 0
# A[x] = A[x-1]^x
# for , where is the symbol for XOR
# You will be given a left and right index . You must determine the XOR sum of the segment of A as
# A[l]^A[l+1]...^A[r].
# For example, A = [0,1,3,0,4,1,7,0,8] . The segment from l=1 to r=4 sums to 1^3^0^4 = 6.
# Print the answer to each question.
# Function Description
# Complete the xorSequence function in the editor below. It should return the integer value calculated.
# xorSequence has the following parameter(s):
# l: the lower index of the range to sum
# r: the higher index of the range to sum
# Input Format
# The first line contains an integer , the number of questions.
# Each of the next lines contains two space-separated integers, and , the inclusive left and right indexes of the
# segment to query.
# Constraints
# 1<=q<=10e5
# 1<l[i]<r[i]<10e15
# Output Format
# On a new line for each test case, print the XOR-Sum of 's elements in the inclusive range between indices and .
# Sample Input 0
# 3
# 2 4
# 2 8
# 5 9
# Sample Output 0
# 7
# 9
# 15
# Explanation 0
# The beginning of our array looks like this: [0,1,3,0,4,1,7,0,8,...]
import math
import os
import random
import re
import sys

# Complete the xorSequence function below.
def xorSequence(l, r):
    def A(x):
        a = x%8
        if(a == 0 or a == 1):
            return x
        if(a == 2 or a == 3):
            return 2
        if(a == 4 or a == 5):
            return x+2
        if(a == 6 or a == 7):
            return 0;
    ans = A(l-1)^A(r)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        lr = input().split()

        l = int(lr[0])

        r = int(lr[1])

        result = xorSequence(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
