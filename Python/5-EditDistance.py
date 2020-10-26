# 5-EditDistance

# Edit Distance
# Given two strings str1 and str2 and below operations that can performed on 
# str1. Find minimum number of edits (operations) required to convert ‘str1’ 
# into ‘str2’.

# Insert
# Remove
# Replace
# All of the above operations are of equal cost.

# Examples:

# Input:   str1 = "geek", str2 = "gesek"
# Output:  1
# We can convert str1 into str2 by inserting a 's'.

# Input:   str1 = "cat", str2 = "cut"
# Output:  1
# We can convert str1 into str2 by replacing 'a' with 'u'.

# Input:   str1 = "sunday", str2 = "saturday"
# Output:  3
# Last three and first characters are same.  We basically
# need to convert "un" to "atur".  This can be done using
# below three operations. 
# Replace 'n' with 'r', insert t, insert a


# What are the subproblems in this case?
# The idea is process all characters one by one staring from either from left
#  or right sides of both strings.
# Let us traverse from right corner, there are two possibilities for every pair 
# of character being traversed.

# m: Length of str1 (first string)
# n: Length of str2 (second string)
# If last characters of two strings are same, nothing much to do. Ignore last
# characters and get count for remaining strings. So we recur for lengths m-1 
# and n-1.
# Else (If last characters are not same), we consider all operations on 
# ‘str1’, consider all three operations on last character of first string, 
# recursively compute minimum cost for all three operations and take minimum 
# of three values.
# Insert: Recur for m and n-1
# Remove: Recur for m-1 and n
# Replace: Recur for m-1 and n-1

def EditDistance(str1,str2,m,n):
	# If first string is empty, the only option is to 
    # insert all characters of second string into first 
	if m==0 :
		return n

	# If second string is empty, the only option is to 
    # remove all characters of first string 
	if n==0:
		return m

	# If last characters of two strings are same, nothing 
    # much to do. Ignore last characters and get count for 
    # remaining strings.
	elif str1[m-1]==str2[n-1]:
		return EditDistance(str1,str2,m-1,n-1)

	# If last characters are not same, consider all three 
    # operations on last character of first string, recursively 
    # compute minimum cost for all three operations and take 
    # minimum of three values. 
	else:
		return 1+min(EditDistance(str1,str2,m,n-1),EditDistance(str1,str2,m-1,n),EditDistance(str1,str2,m-1,n-1))

str1 = "sunday"
str2 = "saturday"
print (EditDistance(str1, str2, len(str1), len(str2)) )		