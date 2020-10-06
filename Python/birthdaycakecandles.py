# You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

# Example

# candles = [4,4,1,3]

# The maximum height candles are  4 units high. There are 2  of them, so return 2.

# Function Description

# Complete the function birthdayCakeCandles in the editor below.

# birthdayCakeCandles has the following parameter(s):

#  ---int candles[n]: the candle heights


# Returns

#  ---int:  the number of candles that are tallest

# Input Format

# The first line contains a single integer,n , the size of candles[].
# The second line contains n space-separated integers, where each integer i  describes the height of candles[i].

# Constraints
#  --- 1<=n<=10^5
#  --- 1<=candles[i]<=10^7

# Sample Input 0

# 4
# 3 2 1 3
# Sample Output 0

# 2

# Explanation 0

# Candle heights are [3,2,1,3]. The tallest candles are 3 units, and there are 2 of them.


#!/bin/python3


import os
import sys


# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):

    res=max(ar)

    count = 0
    ar_len=len(ar)
    for i in range(0,ar_len):
        if(ar[i]==res):
            count+=1


    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
