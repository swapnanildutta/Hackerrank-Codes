'''
Language:- Python-3

Problem link:- https://www.hackerrank.com/contests/oa2021o2/challenges/o-add-upto-a-value/problem


Given an array A of N positive integers and another number X. Determine whether or not there exist two elements in A whose sum is exactly X.

(Using the sliding window technique)

TC: O(n)

Input Format

The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N and X, N is the size of array. The second line of each test case contains N integers representing array elements A[i].

Constraints

1 ≤ T ≤ 100
1 ≤ N ≤ 105
1 ≤ A[i] ≤ 105
Output Format

Print "Yes" if there exist two elements in A whose sum is exactly X, else "No" (without quotes).

Sample Input 0

1
5 10
1 2 4 3 6
Sample Output 0

Yes

'''

n = int(input())
for i in range(n):
    x, y = input().split()
    a = list(map(int, input().strip().split()))[:int(x)]
    i = 0
    j = len(a)-1
    flag = 1
    a.sort()
    while(i<j):
        if(a[i]+a[j]==int(y)):
            print("Yes")
            flag=0
            break
        elif(a[i]+a[j]>int(y)):
            j -= 1
        else:
            i += 1
    if(flag==1):
        print("No")
