'''
Objective
In the previous challenge, we calculated a mean. In this challenge, we practice calculating a weighted mean. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, X, of N integers and an array, W, representing the respective weights of X's elements, calculate and print the weighted mean of X's elements. Your answer should be rounded to a scale of 1 decimal place (i.e.,12.3  format).

Input Format

The first line contains an integer, N, denoting the number of elements in arrays X and W.
The second line contains N space-separated integers describing the respective elements of array X.
The third line contains N space-separated integers describing the respective elements of array W.

Constraints
5 <= N <=50
0 < xi <=100, where xi is the ith element of array X.
0 < wi <= 100, where wi is the ith element of array W.

Output Format

Print the weighted mean on a new line. Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).

Sample Input

5
10 40 30 50 20
1 2 3 4 5

Sample Output

32.0

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
l = list(map(int, input().split()))
w = list(map(int, input().split()))
num = 0
den = 0
for i in range(n):
    num += l[i]*w[i]
    den += w[i]
print(round(num/den,1))