'''
Objective
In this challenge, we practice solving problems based on the Central Limit Theorem. Check out the Tutorial tab for learning materials!

Task
A large elevator can transport a maximum of  pounds. Suppose a load of cargo containing  boxes must be transported via the elevator. The box weight of this type of cargo follows a distribution with a mean of  pounds and a standard deviation of  pounds. Based on this information, what is the probability that all  boxes can be safely loaded into the freight elevator and transported?

Input Format

There are  lines of input (shown below):

9800
49
205
15
The first line contains the maximum weight the elevator can transport. The second line contains the number of boxes in the cargo. The third line contains the mean weight of a cargo box, and the fourth line contains its standard deviation.

If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

Print the probability that the elevator can successfully transport all  boxes, rounded to a scale of  decimal places (i.e.,  format).
'''
import math

def N(mean,std,x):
    return 0.5 + 0.5 * math.erf((x-mean)/(std* 2**0.5))

load = int(input())
n = int(input())
mean = int(input())
std = int(input())

mean1 = n*mean
std1 = math.sqrt(n)*std

print(N(mean1,std1,load))

