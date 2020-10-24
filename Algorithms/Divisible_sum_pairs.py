"""

Name          : Divisible Sum Pais
Category      : Implementation
Difficulty    : Easy
Language      : Python3
Question Link : https://www.hackerrank.com/challenges/the-birthday-bar/problem

"""
"""

You are given an array of  integers, ar=[ar[0],ar[1],....,ar[n-1], and a positive integer,k. Find and print the number of (i , j) pairs where  and ar[i] + ar[j] is divisible by k.

For example, ar = [1 , 2 , 3 , 4 , 5 , 6] and k = 5. Our three pairs meeting the criteria are [1 , 4], [2 , 3] and [4 , 6].

Function Description

Complete the divisibleSumPairs function in the editor below. It should return the integer count of pairs meeting the criteria.

divisibleSumPairs has the following parameter(s):

> n: the integer length of array 
> ar: an array of integers
> k: the integer to divide the pair sum by

Input Format

The first line contains 2 space-separated integers, n and k.
The second line contains n space-separated integers describing the values of ar[ar[0] , ar[1], ..... , ar[n - 1]].

Constraints
> 2 <= n <= 100
> 1 <= k <= 100
> 1 <= ar[i] <= 100

Output Format

Print the number of (i , j) pairs where i < j and a[i] + a[j] is evenly divisible by k.

Sample Input

6 3
1 3 2 6 1 2

Sample Output
5
Explanation

Here are the  valid pairs when k = 3:
> (0 , 2) -> ar[0] + ar[2] = 1 + 2 = 3
> (0 , 5) -> ar[0] + ar[5] = 1 + 2 = 3
> (1 , 3) -> ar[1] + ar[3] = 3 + 6 = 9
> (2 , 4) -> ar[2] + ar[4] = 2 + 1 = 3
> (4 , 5) -> ar[4] + ar[5] = 1 + 2 = 3



"""

n,k = map(int,input().split()) 
a = list(map(int,input().split()))
ans = 0

for i in range(n):
    for j in range(i+1,n):
        if (a[i]+a[j])%k==0: ans+=1

print (ans)
