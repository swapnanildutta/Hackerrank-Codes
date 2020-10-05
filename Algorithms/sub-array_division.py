"""

Name          : Sub-Array Divison
Category      : Implementation
Difficulty    : Easy
Language      : Python3
Question Link : https://www.hackerrank.com/challenges/the-birthday-bar/problem

"""

n = int(input())
s = list(map(int, input().split()))
d, m = map(int, input().split())

ans = 0
for i in range(n-m+1):
    if (sum(s[i:i+m]) == d): ans += 1
        
print(ans)