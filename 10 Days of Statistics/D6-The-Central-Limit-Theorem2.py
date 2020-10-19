'''
Objective
In this challenge, we practice solving problems based on the Central Limit Theorem. We recommend reviewing the Central Limit Theorem Tutorial before attempting this challenge.

Task
The number of tickets purchased by each student for the University X vs. University Y football game follows a distribution that has a mean of  and a standard deviation of .

A few hours before the game starts,  eager students line up to purchase last-minute tickets. If there are only  tickets left, what is the probability that all  students will be able to purchase tickets?

Input Format

There are  lines of input (shown below):

250
100
2.4
2.0
The first line contains the number of last-minute tickets available at the box office. The second line contains the number of students waiting to buy tickets. The third line contains the mean number of purchased tickets, and the fourth line contains the standard deviation.

If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

Print the probability that  students can successfully purchase the remaining  tickets, rounded to a scale of  decimal places (i.e.,  format).
'''

import math

def N(mean,std,x):
    return 0.5 + 0.5 * math.erf((x-mean)/(std* 2**0.5))

load = int(input())
n = int(input())
mean = float(input())
std = float(input())

mean1 = n*mean
std1 = math.sqrt(n)*std

print(N(mean1,std1,load))
