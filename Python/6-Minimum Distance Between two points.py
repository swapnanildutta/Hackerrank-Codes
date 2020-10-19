import sys
def mincost(cost , m , n):
	if m < 0 or n <0:
		return sys.maxsize
	if m == 0 and n ==0:
		return cost[m][n]
	else:
		return cost[m][n] +min(mincost(cost,m-1,n-1), mincost(cost,m-1,n), mincost(cost,m,n-1))
def min(x,y,z):
	if x < y:
		return x if x < z else z
	else:
		return y if y < z else z
list1=[[1,2,3,8],[2,8,2,42],[4,5,6,68],[52,62,68,72]]
print(mincost(list1,3,2))