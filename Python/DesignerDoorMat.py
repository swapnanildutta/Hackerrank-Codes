n,m = map(int,input().split(" "))
str = "WELCOME"
symbol = ".|."

for i in range(0,n):
    if i % 2 != 0:
        print((symbol*i).center(m,"-"))

print(str.center(m,"-"))

i = n-1
while i>=0:
    if i % 2 != 0:
        print((symbol*i).center(m,"-"))
    i-=1
