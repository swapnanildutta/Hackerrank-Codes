'''
Objective
In this challenge, we go further with normal distributions. We recommend reviewing the previous challenge's Tutorial before attempting this problem.

Task
The final grades for a Physics exam taken by a large group of students have a mean of  and a standard deviation of . If we can approximate the distribution of these grades by a normal distribution, what percentage of the students:

1. Scored higher than  (i.e., have a grade>80)?
2. Passed the test (i.e., have a grade>=60)?
3. Failed the test (i.e., have a grade<60)?
Find and print the answer to each question on a new line, rounded to a scale of  decimal places.

Input Format

There are  lines of input (shown below):

70 10
80
60
The first line contains  space-separated values denoting the respective mean and standard deviation for the exam. The second line contains the number associated with question . The third line contains the pass/fail threshold number associated with questions  and .

If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

There are three lines of output. Your answers must be rounded to a scale of 2 decimal places (i.e., 1.23 format):

On the first line, print the answer to question 1 (i.e., the percentage of students having grade>80).
On the second line, print the answer to question 2 (i.e., the percentage of students having grade>=60).
On the third line, print the answer to question 3 (i.e., the percentage of students having grade<60).
'''
import math

def N(mean, std, x):
    return 0.5 + 0.5 * math.erf((x-mean)/(std* 2**0.5))

mean, std = map(int, input().split())
a1 = int(input())
a2 = int(input())

print(round((1 - N(mean, std, a1))*100,2))
print(round((1 - N(mean, std, a2))*100,2))
print(round((N(mean, std, a2))*100,2))
