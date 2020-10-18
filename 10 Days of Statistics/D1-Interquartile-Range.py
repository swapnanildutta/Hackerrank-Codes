'''
Objective
In this challenge, we practice calculating the interquartile range. We recommend you complete the Quartiles challenge before attempting this problem.

Task
The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e., Q3-Q1).

Given an array, X, of n integers and an array, F, representing the respective frequencies of X's elements, construct a data set, S, where each xi occurs at frequency fi. Then calculate and print S's interquartile range, rounded to a scale of 1 decimal place (i.e., 12.3 format).

Tip: Be careful to not use integer division when averaging the middle two elements for a data set with an even number of elements, and be sure to not include the median in your upper and lower data sets.

Input Format

The first line contains an integer, n, denoting the number of elements in arrays X and F.
The second line contains n space-separated integers describing the respective elements of array X.
The third line contains n space-separated integers describing the respective elements of array F.

Constraints
5 <= n <=50
0 < xi <= 100, where xi is the ith element of array X.
0 < sigma(fi) <= 10^3, where fi is the ith element of array F.
The number of elements in S is equal to sigma(F).

Output Format

Print the interquartile range for the expanded data set on a new line. Round your answer to a scale of 1 decimal place (i.e., 12.3 format).

Sample Input

6
6 12 8 10 20 16
5 4 3 2 1 5

Sample Output

9.0

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

from statistics import median
n=int(input())
x=list(map(int,input().split()))
f=list(map(int,input().split()))
arr = []
for i in range(n):
    arr += [x[i]]*f[i]
arr.sort()
t=len(arr)//2
if len(arr)%2==0:
    L=arr[:t]
    U=arr[t:]
else:
    L=arr[:t]
    U=arr[t+1:]

print(round(float(median(U)-median(L)),1))
