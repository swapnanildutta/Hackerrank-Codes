"""

Name          : Grading Students
Category      : Implementation
Difficulty    : Easy
Language      : Python3
Question Link : https://www.hackerrank.com/challenges/grading/problem

"""

n = int(input().strip())
for _ in range(n):
    x = int(input().strip())
    
    if x >= 38 and x % 5 > 2:
            while x % 5 != 0: x += 1
    print(x)