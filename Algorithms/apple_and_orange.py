"""

Name          : Apple and Orange
Category      : Implementation
Difficulty    : Easy
Language      : Python3
Question Link : https://www.hackerrank.com/challenges/apple-and-orange/problem

"""

s,t = map(int,input().split())
a,b = map(int, input().split())
m,n = map(int, input().split())
apple = map(int,input().split())
orange = map(int,input().split())
apple_count=0
for i in apple:
    if s<=a+i<=t: apple_count+=1

orange_count=0
for i in orange:
    if s<=b+i<=t: orange_count+=1

print(apple_count)
print(orange_count)