# Longest Common Subsequence

# reference:https://www.ics.uci.edu/~eppstein/161/960229.html
# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/

# LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
# LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

# Method-1
# 1) Optimal Substructure:
# If last characters of both sequences match (or X[m-1] == Y[n-1]) then
# L(X[0..m-1], Y[0..n-1]) = 1 + L(X[0..m-2], Y[0..n-2])

# If last characters of both sequences do not match (or X[m-1] != Y[n-1]) then
# L(X[0..m-1], Y[0..n-1]) = MAX ( L(X[0..m-2], Y[0..n-1]), L(X[0..m-1], Y[0..n-2]) )


def LongestCommonSubsequence(str1,str2,m,n):
	if m == 0 or n == 0:
		return 0
	if str1[m-1]==str2[n-1]:
		return 1 + LongestCommonSubsequence(str1,str2,m-1,n-1)
	else:
		return max(LongestCommonSubsequence(str1,str2,m-1,n),LongestCommonSubsequence(str1,str2,m,n-1))

X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", LongestCommonSubsequence(X , Y, len(X), len(Y)))

#method -2
# refernce:https://www.youtube.com/watch?v=tABtJbLOQho&list=PLamzFoFxwoNjtJZoNNAlYQ_Ixmm2s-CGX&index=4
# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/

def LongestCommonSubsequence2(str1,str2):
	n=len(str1)
	m=len(str2)
	aux_list=[[0]*(n+1) for j in range(m+1)]
	for i in range(m+1):
		for j in range(n+1):
			if i==0 or j==0:
				aux_list[i][j]=0
			elif str1[i-1]==str2[j-1]:
				aux_list[i][j]=1+aux_list[i-1][j-1]
			else:
				aux_list[i][j]=max(aux_list[i-1][j],aux_list[i][j-1])
	return aux_list[m][n]

print(LongestCommonSubsequence2("AGGTAB","GXTXAYB"))


def lcs(X , Y): 
    # find the length of the strings 
    m = len(X) 
    n = len(Y) 
  
    # declaring the array for storing the dp values 
    L = [[None]*(n+1) for i in range(m+1)] 
  
    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return L[m][n] 
#end of function lcs 
  
  
# Driver program to test the above function 
# X = "AGGTAB"
# Y = "GXTXAYB"
# print ("Length of LCS is ", lcs(X, Y) )
#---------------------------------------------------------------------------
# In case of need of longest common sequence we need to back track the nos
# for aux_list
# index = L[m][n] 
  
#     # Create a character array to store the lcs string 
#     lcs = [""] * (index+1) 
#     lcs[index] = "" 
  
#     # Start from the right-most-bottom-most corner and 
#     # one by one store characters in lcs[] 
#     i = m 
#     j = n 
#     while i > 0 and j > 0: 
  
#         # If current character in X[] and Y are same, then 
#         # current character is part of LCS 
#         if X[i-1] == Y[j-1]: 
#             lcs[index-1] = X[i-1] 
#             i-=1
#             j-=1
#             index-=1
  
#         # If not same, then find the larger of two and 
#         # go in the direction of larger value 
#         elif L[i-1][j] > L[i][j-1]: 
#             i-=1
#         else: 
#             j-=1
  
#     print "LCS of " + X + " and " + Y + " is " + "".join(lcs)  

#---------------------------------------------------------------------------



# Longest Common Anagram Subsequence

# reference:https://www.geeksforgeeks.org/longest-common-anagram-subsequence/
# Given two strings str1 and str2 of length n1 and n2 respectively. 
# The problem is to find the length of the longest subsequence which is 
# present in both the strings in the form of anagrams.
# Note: The strings contain only lowercase letters.
# Examples:
# Input : str1 = "abdacp", str2 = "ckamb"
# Output : 3
# Subsequence of str1 = abc
# Subsequence of str2 = cab
#           OR
# Subsequence of str1 = bac
# Subsequence of str2 = cab

# These are longest common anagram subsequences.
# Input : str1 = "abbcfke", str2 = "fbaafbly"
# Output : 4

# Approach: Create two hash tables say freq1 and freq2. Store frequencies of 
# each character of str1 in freq1. Likewise, store frequencies of each 
# character of str2 in freq2. Initilaize len = 0. Now, for each lowercase 
# letter finds its lowest frequency from the two hash tables and accumulate 
# it to len.

# Python 3 implementation to find  
# the length of the longest common  
# anagram subsequence   
# SIZE = 26
  
# # function to find the length of the  
# # longest common anagram subsequence 
# def longCommomAnagramSubseq(str1, str2,n1, n2): 
#     # List for storing frequencies  
#     # of each character 
#     freq1 = [0] * SIZE 
#     freq2 = [0] * SIZE 
#     l = 0
#     # calculate frequency of each  
#     # character of 'str1[]' 
#     for i in range(n1): 
#         freq1[ord(str1[i]) -
#               ord('a')] += 1
#     # calculate frequency of each 
#     # character of 'str2[]' 
#     for i in range(n2) :  
#         freq2[ord(str2[i]) - 
#               ord('a')] += 1
#     # for each character add its  
#     # minimum frequency out of  
#     # the two strings in 'len' 
#     for i in range(SIZE):  
#         l += min(freq1[i], freq2[i]) 
#     # required length 
#     return l                              
  
# # Driver Code 
# if __name__ == "__main__": 
      
#     str1 = "abdacp"
#     str2 = "ckamb"
#     n1 = len(str1) 
#     n2 = len(str2) 
#     print("Length = ",  
#            longCommomAnagramSubseq(str1, str2,  
#                                        n1, n2)) 
#---------------------------------------------------------------------------
# LCS (Longest Common Subsequence) of three strings

# Given 3 strings of all having length < 100,the task is to find the longest 
# common sub-sequence in all three given sequences.
# Examples:
# Input : str1 = "geeks"  
#         str2 = "geeksfor"  
#         str3 = "geeksforgeeks"
# Output : 5
# Longest common subsequence is "geeks"
# i.e., length = 5

# Input : str1 = "abcd1e2"  
#         str2 = "bc12ea"  
#         str3 = "bd1ea"
# Output : 3
# Longest common subsequence is "b1e" 
# i.e. length = 3.
# This problem is simply an extension of LCS

# Let the input sequences be X[0..m-1], Y[0..n-1] and Z[0..o-1] of lengths 
# m, n and o respectively. And let L(X[0..m-1], Y[0..n-1], Z[0..o-1]) be the 
# lengths of LCS of the three sequences X, Y and Z. Following is the 
# implementation:
# The idea is to take a 3D array to store the 
# length of common subsequence in all 3 given 
# sequences i. e., L[m + 1][n + 1][o + 1]

# 1- If any of the string is empty then there
#    is no common subsequence at all then
#            L[i][j][k] = 0

# 2- If the characters of all sequences match
#    (or X[i] == Y[j] ==Z[k]) then
#         L[i][j][k] = 1 + L[i-1][j-1][k-1]

# 3- If the characters of both sequences do 
#    not match (or X[i] != Y[j] || X[i] != Z[k] 
#    || Y[j] !=Z[k]) then
#         L[i][j][k] = max(L[i-1][j][k], 
#                          L[i][j-1][k], 
#                          L[i][j][k-1])
#---------------------------------------------------------------------------
# Longest common subsequence with permutations allowed

# Given two strings in lowercase, find the longest string whose permutations 
# are subsequences of given two strings. The output longest string must be 
# sorted.

# Examples:
# Input  :  str1 = "pink", str2 = "kite"
# Output : "ik" 
# The string "ik" is the longest sorted string 
# whose one permutation "ik" is subsequence of
# "pink" and another permutation "ki" is 
# subsequence of "kite". 

# Input  : str1 = "working", str2 = "women"
# Output : "now"

# Input  : str1 = "geeks" , str2 = "cake"
# Output : "ek"

# Input  : str1 = "aaaa" , str2 = "baba"
# Output : "aa"

# The idea is to count characters in both strings.
# calculate frequency of characters for each string and store them in their 
# respective count arrays, say count1[] for str1 and count2[] for str2.
# Now we have count arrays for 26 characters. So traverse count1[] and for any 
# index ‘i’ append character (‘a’+i) in resultant string ‘result’ by 
# min(count1[i], count2[i]) times.
# Since we traverse count array in ascending order, our final string 
# characters will be in sorted order.

# Python 3 program to find LCS 
# with permutations allowed 
  
# Function to calculate longest string 
# str1     --> first string 
# str2     --> second string 
# count1[] --> hash array to calculate frequency 
#               of characters in str1 
# count[2] --> hash array to calculate frequency 
#               of characters in str2 
# result --> resultant longest string whose 
# permutations are sub-sequence  
# of given two strings 
def longestString(str1, str2): 
  
    count1 = [0] * 26
    count2 = [0] * 26
  
    # calculate frequency of characters 
    for i in range( len(str1)): 
        count1[ord(str1[i]) - ord('a')] += 1
    for i in range(len(str2)): 
        count2[ord(str2[i]) - ord('a')] += 1
  
    # Now traverse hash array 
    result = "" 
    for i in range(26): 
  
        # append character ('a'+i) in  
        # resultant string 'result' by  
        # min(count1[i],count2i]) times 
        for j in range(1, min(count1[i], 
                              count2[i]) + 1): 
            result = result + chr(ord('a') + i) 
  
    print(result) 
  
# Driver Code 
# if __name__ == "__main__": 
      
#     str1 = "geeks"
#     str2 = "cake"
#     longestString(str1, str2) 

#---------------------------------------------------------------------------
# Longest Subsequence with at least one common digit in every element

# Given an array. The task is to find the length of the longest subsequence 
# in which all elements must have at least one digit in common.

# Examples:

# Input : arr[] = { 11, 12, 23, 74, 13 }
# Output : 3
# Explanation: The elements 11, 12, and 13 have the digit ‘1’ as common.
#  So it is the required longest sub-sequence.



# Input : arr[] = { 12, 90, 67, 78, 45 }
# Output : 2

# Normal Approach: Find all the subsequences of the array and find the 
# subsequence in which every element must have a common digit. Then we 
# have to find the longest such subsequence and print the length of that 
# subsequence. This method will take exponential time complexity.

# reference:https://www.geeksforgeeks.org/longest-subsequence-with-at-least-one-common-digit-in-every-element/
#---------------------------------------------------------------------------