# Title: Sansa and XOR
# Difficulty: Medium
# Points: 30

# Sansa has an array. She wants to find the value obtained by XOR-ing the contiguous subarrays, followed by XOR-ing the values thus obtained. Determine this value.

# For example, if arr = [3, 4, 5]:

# Subarray	Operation	Result
# 3		None		3
# 4		None		4
# 5		None		5
# 3,4		3 XOR 4		7
# 4,5		4 XOR 5		1
# 3,4,5		3 XOR 4 XOR 5	2
# Now we take the resultant values and XOR them together:
# 3 XOR 4 XOR 5 XOR 7 XOR 1 XOR 2 = 6

# Function Description

# Complete the sansaXor function in the editor below. It should return an integer that represents the results of the calculations.

# sansaXor has the following parameter(s):

# arr: an array of integers

# Input Format

# The first line contains an integer t, the number of the test cases.

# Each of the next t pairs of lines is as follows:
# - The first line of each test case contains an integer n, the number of elements in arr.
# - The second line of each test case contains n space-separated integers arr[i].

# Constraints

#     1 <= t <= 5
#     2 <= n <= 10^5
#     1 <= arr[i] <= 10^8

# Output Format

# Print the results of each test case on a separate line.

# Sample Input 0

# 2
# 3
# 1 2 3
# 4
# 4 5 7 5

# Sample Output 0

# 2
# 0

# Explanation 0

# Test case 0:
# 1 XOR 2 XOR 3 XOR (1 XOR 2) XOR (2 XOR 3) XOR (1 XOR 2 XOR 3) = 2

# Test case 1:
# 4 XOR 5 XOR 7 XOR 5 XOR (4 XOR 5) XOR (5 XOR 7) XOR (7 XOR 5) XOR (4 XOR 5 XOR 7) XOR (5 XOR 7 XOR 5) XOR (4 XOR 5 XOR 7 XOR 5) = 0

# Sample Input 1

# 2
# 3
# 98 74 12
# 3
# 50 13 2
# Sample Output 1

# 110
# 48
# Explanation 1

# Test Case 0:
# 98 XOR 74 XOR 12 (98 XOR 74) XOR (74 XOR 12) XOR (98 XOR 74 XOR 12) = 110

# Test Case 1:
# 50 XOR 13 XOR 2 XOR (50 XOR 13) XOR (13 XOR 2) XOR (50 XOR 13 XOR 2) = 48

def sansaXor(arr):
    n=len(arr)
    if n%2==0:
        return 0
    else:
        ans=0
        for i in range(0,n,2):
            ans=ans^arr[i]
        return ans


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split(' ')))
        print(sansaXor(arr))