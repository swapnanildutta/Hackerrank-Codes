"""

Name          : Between Two Sets
Category      : Implementation
Difficulty    : Easy
Language      : Python3
Question Link : https://www.hackerrank.com/challenges/between-two-sets/problem

"""

aa=bb=ct=0
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

for i in range(max(a),min(b)+1):
    for j in a:
        if i%j!=0: break
    else:
        for k in b:
            if k%i!=0: break
        else: ct+=1
print(ct)
