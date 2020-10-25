'''
Objective
In this challenge, we learn about normal distributions. Check out the Tutorial tab for learning materials!

Task
In a certain plant, the time taken to assemble a car is a random variable, , having a normal distribution with a mean of  hours and a standard deviation of  hours. What is the probability that a car can be assembled at this plant in:

Less than  hours?
Between  and  hours?
Input Format

There are  lines of input (shown below):

20 2
19.5
20 22
The first line contains  space-separated values denoting the respective mean and standard deviation for . The second line contains the number associated with question . The third line contains  space-separated values describing the respective lower and upper range boundaries for question .

If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

There are two lines of output. Your answers must be rounded to a scale of  decimal places (i.e.,  format):

On the first line, print the answer to question  (i.e., the probability that a car can be assembled in less than  hours).
On the second line, print the answer to question  (i.e., the probability that a car can be assembled in between  to  hours).
'''

import math

def N(mean, std, x):
        return 0.5 + 0.5 * math.erf((x-mean)/(std* 2**0.5))

mean, std = map(int, input().split())
a1 = float(input())
a2,b2 = map(float, input().split())

print(round(N(mean, std, a1),3))

print(round(N(mean,std,b2)-N(mean,std,a2),3))
