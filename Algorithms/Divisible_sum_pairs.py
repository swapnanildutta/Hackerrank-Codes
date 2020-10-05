"""

Name          : Divisible Sum Pais
Category      : Implementation
Difficulty    : Easy
Language      : Python3
Question Link : https://www.hackerrank.com/challenges/the-birthday-bar/problem

"""

n,k = map(int,input().split()) 
a = list(map(int,input().split()))
ans = 0

for i in range(n):
    for j in range(i+1,n):
        if (a[i]+a[j])%k==0: ans+=1

print (ans)