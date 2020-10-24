def sumofdigits(n):
	sum=0
	temp=0
	while n>0:
		num=n%10
		n=n//10
		sum=sum+num
	return sum

def count(n,sum):
	count=0
	for i in range(10,10**n+1):
		if sumofdigits(i) == sum:
			count+=1
	return count

print(count(2,5))
# print(sumofdigits(14))