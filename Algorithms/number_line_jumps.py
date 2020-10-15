"""

Name          : Number Line Jumps
Category      : Implementation
Difficulty    : Easy
Language      : Python3
Question Link : https://www.hackerrank.com/challenges/kangaroo/problem

"""

x1,v1,x2,v2 = map(int, input().split())
if v1==v2: print ('NO')
else:
    if (x1-x2+v2-v1)%(v2-v1)==0 and (x1-x2+v2-v1)/(v2-v1)>0: print('YES'')
    else: print ('NO')