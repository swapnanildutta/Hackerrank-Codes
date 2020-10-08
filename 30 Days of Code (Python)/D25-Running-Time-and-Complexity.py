'''
Objective
Today we're learning about running time! Check out the Tutorial tab for learning materials and an instructional video!

Task
A prime is a natural number greater than
that has no positive divisors other than and itself. Given a number, , determine and print whether it's or

.

Note: If possible, try to come up with a
primality algorithm, or see what sort of optimizations you come up with for an

algorithm. Be sure to check out the Editorial after submitting your code!

Input Format

The first line contains an integer,
, the number of test cases.
Each of the subsequent lines contains an integer,

, to be tested for primality.

Constraints

Output Format

For each test case, print whether
is or

on a new line.

Sample Input

3
12
5
7

Sample Output

Not prime
Prime
Prime

Explanation

Test Case 0:
.
is divisible by numbers other than and itself (i.e.: , , ), so we print

on a new line.

Test Case 1:
.
is only divisible and itself, so we print

on a new line.

Test Case 2:
.
is only divisible and itself, so we print on a new line.
'''

import math

nums=list()
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        nums.append(int(input()))
    for _ in nums:
        if _ in (0, 1):
            print('Not prime')
        else:
            m=0
            for a in range(2,int(math.sqrt(_))+1):
                if _%a == 0:
                    m+=1
            if m == 0:
                print('Prime')
            else:
                print('Not prime')
