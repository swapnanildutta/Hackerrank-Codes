"""

Name          : Breaking the records
Category      : Implementation
Difficulty    : Easy
Language      : Python3
Question Link : https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

"""

n = int(input())
score = list(map(int, input().split()))
a = b = score[0]
r1 = r2 = 0

for i in score[1:]:
    if i > a:
        a = i
        r1 += 1
    if i < b:
        b = i
        r2 += 1
print(r1,r2)