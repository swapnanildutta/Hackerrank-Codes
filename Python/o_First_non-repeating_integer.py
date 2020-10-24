'''
Given an integer array, the task is to find and print the first non-repeating element in it.

Input Format

First line of the input contains an integer T, denoting the number of test cases. 
Then T test cases follow.
Each test case consists of two lines.
First line of each test case contains integer N denoting the size of array. 
Second line of each test case contains N space separated integers (Ki) denoting the elements of the array.

Constraints

1<= T <= 100
2<= N <= 20 
1<= K <= 50

Output Format

Integer

Sample Input 0

1
5
1 1 2 2 3
Sample Output 0

3

'''


n = int(input())
for i in range(n):
    s = int(input())
    a = list(map(int,input().strip().split()))[:s]
    for i in range(len(a)): 
        j = 0
        while(j < len(a)): 
            if (i != j and a[i] == a[j]): 
                break
            j += 1
        if (j == len(a)): 
            print(a[i]) 
