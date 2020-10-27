# Title: Longest Common Subsequence
# Difficulty: Medium
# Points: 55
# Category: Algorithms - Dynamic Programming

# A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. Longest common subsequence (LCS) of 2 sequences is a subsequence, with maximal length, which is common to both the sequences.

# Given two sequences of integers, A = [a[1], a[2],...,a[n]] and B = [b[1], b[2],...,b[m]], find the longest common subsequence and print it as a line of space-separated integers. If there are multiple common subsequences with the same maximum length, print any one of them.

# In case multiple solutions exist, print any of them. It is guaranteed that at least one non-empty common subsequence will exist.

# Function Description

# Complete the longestCommonSubsequence function in the editor below. It should return an integer array of a longest common subsequence.

# longestCommonSubsequence has the following parameter(s):

# a: an array of integers
# b: an array of integers

# Input Format

# The first line contains two space separated integers n and m, the sizes of sequences A and B.
# The next line contains n space-separated integers A[i].
# The next line contains m space-separated integers B[j].

# Constraints

# 1 <= n,m <= 100

# 0 <= a[i],b[j] < 1000


# Output Format

# Print the longest common subsequence as a series of space-separated integers on one line. In case of multiple valid answers, print any one of them.

# Sample Input

# 5 6
# 1 2 3 4 1
# 3 4 1 2 1 3

# Sample Output

# 1 2 3

# Explanation

# There is no common subsequence with length larger than 3. And "1 2 3", "1 2 1", "3 4 1" are all correct answers.


def getLCSval(a,b,LCS):
    val=[]
    n1,n2=len(LCS),len(LCS[0])
    i,j=n1-1,n2-1
    while i>0 and j>0:
        if a[i-1]==b[j-1]:
            val.insert(0,a[i-1])
            i-=1
            j-=1
        elif LCS[i-1][j]>LCS[i][j-1]:
            i-=1
        else:
            j-=1
    return val

def longestCommonSubsequence(a, b):
    n1,n2=len(a),len(b)
    LCS = [[0]*(n2+1) for i in range(n1+1)]
    for i in range(n1+1):
        for j in range(n2+1):
            if a[i-1]==b[j-1]:
                LCS[i][j]=LCS[i-1][j-1]+1
            else:
                LCS[i][j]=max(LCS[i-1][j],LCS[i][j-1])
    val=getLCSval(a,b,LCS)
    return val

if __name__ == "__main__":
    n, m = map(int,input().split(' '))
    a = list(map(int,input().split(' ')))
    b = list(map(int,input().split(' ')))
    result = longestCommonSubsequence(a, b)
    print(' '.join(map(str, result)))