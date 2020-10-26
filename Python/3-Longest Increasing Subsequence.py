# Longest Increasing Subsequence
# We have discussed Overlapping Subproblems and Optimal Substructure properties.

# Let us discuss Longest Increasing Subsequence (LIS) problem as an example 
# problem that can be solved using Dynamic Programming.
# The Longest Increasing Subsequence (LIS) problem is to find the length of 
# the longest subsequence of a given sequence such that all elements of the 
# subsequence are sorted in increasing order. For example, the length of LIS
# for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS 
# is {10, 22, 33, 50, 60, 80}.
# longest-increasing-subsequence

# More Examples:

# Input  : arr[] = {3, 10, 2, 1, 20}
# Output : Length of LIS = 3
# The longest increasing subsequence is 3, 10, 20

# Input  : arr[] = {3, 2}
# Output : Length of LIS = 1
# The longest increasing subsequences are {3} and {2}

# Input : arr[] = {50, 3, 10, 7, 40, 80}
# Output : Length of LIS = 4
# The longest increasing subsequence is {3, 7, 40, 80}

#Method 1 :https://youtu.be/Ns4LCeeOFS4
#(nlogn)

def LongestIncreasingSequence(list1):
	n=len(list1)
	list2=[1 for i in range(n)]
	for i in range(1,n):
		for j in range(i):
			if list1[i]>list1[j] and list2[i]<list2[j]+1:
				list2[i]=list2[j]+1
	return max(list2)

print(LongestIncreasingSequence([50, 3, 10, 7, 40, 80]))
