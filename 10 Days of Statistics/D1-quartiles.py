'''
Objective
In this challenge, we practice calculating quartiles. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, X, of n integers, calculate the respective first quartile (Q1), second quartile (Q2), and third quartile (Q3). It is guaranteed that Q1, Q2, and Q3 are integers.

Input Format

The first line contains an integer, n, denoting the number of elements in the array.
The second line contains n space-separated integers describing the array's elements.

Constraints
5 <= n <=50
0 < xi <=100, where xi is the ith element of the array.

Output Format

Print 3 lines of output in the following order:

The first line should be the value of Q1.
The second line should be the value of Q2.
The third line should be the value of Q3.

Sample Input

9
3 7 8 5 12 14 21 13 18

Sample Output

6
12
16

'''


# Enter your code here. Read input from STDIN. Print output to STDOUT

def median(l):
    # l = sorted(l)
    n = len(l)
    if n%2==0:
        return int((l[int(n/2)-1]+l[int(n/2)])/2)
    else:
        return int(l[int(n/2)])

m = int(input())
ls = list(map(int, input().split()))
ls = sorted(ls)

if(m%2==0):
    lh = ls[:int(m/2)]
    uh = ls[int(m/2):]
else:
    lh = ls[:int(m/2)]
    uh = ls[int(m/2)+1:]

print(median(lh))
print(median(ls))
print(median(uh))