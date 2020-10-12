# Problem
# Write a function that takes two parameters n and k and returns the 
# value of Binomial Coefficient C(n, k). For example, your function 
# should return 6 for n = 4 and k = 2, and it should return 10 for 
# n = 5 and k = 2.


# def bio(n,k):
# 	if k == 0 or k == n:
# 		return 1 
# 	else:
# 		return bio(n-1,k-1) + bio(n-1,k)

# print(bio(4,2))

# Using Overlapping Structure


# MY TRY
# def Bionomial(n,k):
# 	if n == k or k == 0:
# 		lookup[[n,k]]=1
# 		return lookup[(n,k)]
# 	if lookup[[n,k]] == None:
# 		return Bionomial(n-1,k-1) + Bionomial(n-1,k)
# lookup = [None]*101
# print(Bionomial(4,2))

# ACTUAL ONCE IS THIS ONE


# print(Bionimal(4,2))



# def binomialCoef(n, k): 
#     C = [[0 for x in range(k+1)] for x in range(n+1)] 
  
#     # Calculate value of Binomial Coefficient in bottom up manner 
#     for i in range(n+1): 
#         for j in range(min(i, k)+1): 
#             # Base Cases 
#             if j == 0 or j == i: 
#                 C[i][j] = 1
  
#             # Calculate value using previously stored values 
#             else: 
#                 C[i][j] = C[i-1][j-1] + C[i-1][j]
  
#     return C[n][k] 

# print(binomialCoef(4,2))




def BionimalCoefficient(n,k):
	if  k==n or k==0:
		return 1
	else:
		return BionimalCoefficient(n-1,k-1)+BionimalCoefficient(n-1,k)
print(BionimalCoefficient(4,2))

# reference:https://www.geeksforgeeks.org/binomial-coefficient-dp-9/