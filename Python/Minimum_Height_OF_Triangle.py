'''
Given integers b and a , find the smallest integer h, such that there exists a triangle of height h, base b, having an area of at least a.

link : https://www.hackerrank.com/challenges/lowest-triangle/problem

'''
import math

b, a = map(int, input().split())

h = (2*a)/(b)

if h > int(h):
    print(math.ceil(h))
else:
    print("%.0f" % h)
