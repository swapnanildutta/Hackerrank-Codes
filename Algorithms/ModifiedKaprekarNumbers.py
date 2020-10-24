# Title: Modified Kaprekar Numbers
# Difficulty: Easy
# Points: 30
# Category: Algorithms - Implementation

# A modified Kaprekar number is a positive whole number with a special property. If you square it, then split the number into two integers and sum those integers, you have the same value you started with.

# Consider a positive whole number n with d digits. We square n to arrive at a number that is either 2*d digits long or (2*d)-1 digits long. Split the string representation of the square into two parts, l and r. The right hand part, r must be d digits long. The left is the remaining substring. Convert those two substrings back to integers, add them and see if you get n.

# For example, if n=5, d=1 then n^2 = 25. We split that into two strings and convert them back to integers 2 and 5. We test 2+5=7!=5, so this is not a modified Kaprekar number. If n=9, still d=1, and n^2=81. This gives us 1+8=9, the original n.

# Note: r may have leading zeros.

# Here's an explanation from Wikipedia about the ORIGINAL Kaprekar Number (spot the difference!): (https://en.wikipedia.org/wiki/Kaprekar_number)

# In mathematics, a Kaprekar number for a given base is a non-negative integer, the representation of whose square in that base can be split into two parts that add up to the original number again. For instance, 45 is a Kaprekar number, because 45² = 2025 and 20+25 = 45.
# Given two positive integers p and q where p is lower than q, write a program to print the modified Kaprekar numbers in the range between  and , inclusive.

# Function Description

# Complete the kaprekarNumbers function in the editor below. It should print the list of modified Kaprekar numbers in ascending order.

# kaprekarNumbers has the following parameter(s):

# p: an integer
# q: an integer
# Input Format

# The first line contains the lower integer limit p.
# The second line contains the upper integer limit q.

# Note: Your range should be inclusive of the limits.

# Constraints

# 0 < p < q < 100000

# Output Format

# Output each modified Kaprekar number in the given range, space-separated on a single line. If no modified Kaprekar numbers exist in the given range, print INVALID RANGE.

# Sample Input

# 1
# 100

# Sample Output

# 1 9 45 55 99

# Explanation

# 1, 9, 45, 55, and 99 are the Kaprekar Numbers in the given range.


# ----------------------------------------------------
# ----------------Solution in Python 3----------------
# ----------------------------------------------------

def kaprekarNumbers(p, q):
    kaprekar = []
    if p == 1:
        kaprekar.append(1)
        p = 4
    for i in range(p,q+1):
        k = str(i*i)
        l = len(k)
        rem = l-len(str(i))
        l = k[:rem]
        l = int(l)
        r = k[rem:]
        r = int(r)
        if l+r==i:
            kaprekar.append(i)
    if len(kaprekar)==0:
        print("INVALID RANGE")
    else:
        for i in kaprekar:
            print(i,end = " ")

if __name__ == '__main__':
    p = int(input())
    q = int(input())
    kaprekarNumbers(p, q)