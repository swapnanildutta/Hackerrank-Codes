'''
Objective
In this challenge, we practice calculating standard deviation. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, X, of N integers, calculate and print the standard deviation. Your answer should be in decimal form, rounded to a scale of 1 decimal place (i.e., 12.3 format). An error margin of +-0.1 will be tolerated for the standard deviation.

Input Format

The first line contains an integer, N, denoting the number of elements in the array.
The second line contains N space-separated integers describing the respective elements of the array.

Constraints
5 <= N <= 100
0 < xi <= 10^5, where xi is the ith element of array X.

Output Format

Print the standard deviation on a new line, rounded to a scale of 1 decimal place (i.e., 12.3 format).

Sample Input

5
10 40 30 50 20

Sample Output

14.1
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
x = list(map(int,input().split()))

mean = sum(x)/n

x = [(i-mean)**2 for i in x]
sd = (sum(x)/n)**(1/2)
print(round(sd,1))