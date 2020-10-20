# Given a value N, if we want to make change for N cents, and we 
# have infinite supply of each of S = { S1, S2, .. , Sm} valued 
# coins, how many ways can we make the change? The order of coins 
# doesn’t matter.

# For example, for N = 4 and S = {1,2,3}, there are four 
# solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should 
# be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: 
# {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output 
# should be 5.


# Recursive Python3 program for 
# coin change problem. 
  
# Returns the count of ways we can sum 
# S[0...m-1] coins to get sum n 
def count(S, m, n ): 
  
    # If n is 0 then there is 1 
    # solution (do not include any coin) 
    if (n == 0): 
        return 1
  
    # If n is less than 0 then no 
    # solution exists 
    if (n < 0): 
        return 0; 
  
    # If there are no coins and n 
    # is greater than 0, then no 
    # solution exist 
    if (m <=0 and n >= 1): 
        return 0
  
    # count is sum of solutions (i)  
    # including S[m-1] (ii) excluding S[m-1] 
    return count( S, m - 1, n ) + count( S, m, n-S[m-1] ); 
  
# Driver program to test above function 
arr = [1, 2, 3] 
m = len(arr) 
print(count(arr, m, 4)) 
  
# This code is contributed by Smitha Dinesh Semwal 


# It should be noted that the above function computes the same 
# subproblems again and again.

# Dynamic Programming Python implementation of Coin  
# Change problem 
def count(S, m, n): 
    # We need n+1 rows as the table is constructed  
    # in bottom up manner using the base case 0 value 
    # case (n = 0) 
    table = [[0 for x in range(m)] for x in range(n+1)] 
  
    # Fill the entries for 0 value case (n = 0) 
    for i in range(m): 
        table[0][i] = 1
  
    # Fill rest of the table entries in bottom up manner 
    for i in range(1, n+1): 
        for j in range(m): 
  
            # Count of solutions including S[j] 
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
  
            # Count of solutions excluding S[j] 
            y = table[i][j-1] if j >= 1 else 0
  
            # total count 
            table[i][j] = x + y 
  
    return table[n][m-1] 
  
# Driver program to test above function 
arr = [1, 2, 3] 
m = len(arr) 
n = 4
print(count(arr, m, n))



# references:https://www.geeksforgeeks.org/coin-change-dp-7/
# https://www.youtube.com/watch?v=L27_JpN6Z1Q

#--------------------------------------------------------------------

# Given two coins of denominations “X” and “Y” respectively, find the 
# largest amount that cannot be obtained using these two coins 
# (assuming infinite supply of coins) followed by the total number 
# of such non obtainable amounts, if no such value exists print “NA”.

# Examples :

# Input : X=2, Y=5  
# Output: Largest amount = 3
#         Total count  = 2
# We cannot represent 1 and 3 from infinite supply
# of given two coins. The largest among these 2 is 3.
# We can represent all other amounts for example 13
# can be represented 2*4 + 5.

# Input : X=5, Y=10
# Output: NA
# There are infinite number of amounts that cannot
# be represented by these two coins.



# This general problem for n coins is known as classic Forbenius coin 
# problem.

# When the number of coins is two, there is 
# explicit formula if GCD is not 1. The formula
# is:
#   Largest amount A = (X * Y) - (X + Y)
#   Total amount = (X -1) * (Y - 1) /2 

def gcd(a, b): 
    while (a != 0): 
        c = a; 
        a = b % a; 
        b = c; 
      
    return b; 
  
# Function to print the desired output 
def forbenius(X, Y): 
  
    # Solution doesn't exist  
    # if GCD is not 1 
    if (gcd(X, Y) != 1): 
        print("NA"); 
        return; 
  
    # Else apply the formula 
    A = (X * Y) - (X + Y); 
    N = (X - 1) * (Y - 1) // 2; 
  
    print("Largest Amount =", A); 
    print("Total Count =", N); 
  
# Driver Code 
X = 2;  
Y = 5; 
forbenius(X, Y); 
  
X = 5;  
Y = 10; 
print(""); 
forbenius(X, Y); 
#--------------------------------------------------------------------