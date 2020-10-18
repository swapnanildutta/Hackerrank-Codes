'''
Objective
In this challenge, we practice calculating the Pearson correlation coefficient. Check out the Tutorial tab for learning materials!

Task
Given two -element data sets,  and , calculate the value of the Pearson correlation coefficient.

Input Format

The first line contains an integer, , denoting the size of data sets  and .
The second line contains  space-separated real numbers (scaled to at most one decimal place), defining data set .
The third line contains  space-separated real numbers (scaled to at most one decimal place), defining data set .

Constraints

, where  is the  value of data set .
, where  is the  value of data set .
Data set  contains unique values.
Data set  contains unique values.
Output Format

Print the value of the Pearson correlation coefficient, rounded to a scale of  decimal places.

Sample Input

10
10 9.8 8 7.8 7.7 7 6 5 4 2 
200 44 32 24 22 17 15 12 8 4
Sample Output

0.612
Explanation

The mean and standard deviation of data set  are:

The mean and standard deviation of data set  are:

We use the following formula to calculate the Pearson correlation coefficient:
'''
n = int(input())

X = list(map(float, input().split()))
Y = list(map(float, input().split()))

mx = sum(X)/n
my = sum(Y)/n

stdx = (sum([(i - mx)**2 for i in X]) / n)**0.5
stdy = (sum([(i - my)**2 for i in Y]) / n)**0.5


covariance = sum([(X[i] - mx) * (Y[i] - my) for i in range(n)])
correlation_coefficient = covariance / (n * stdx * stdy)

print(round(correlation_coefficient,3))
