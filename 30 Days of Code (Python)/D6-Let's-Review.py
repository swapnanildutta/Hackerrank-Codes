'''
Objective
Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given a string,
, of length that is indexed from to , print its even-indexed and odd-indexed characters as

space-separated strings on a single line (see the Sample below for more detail).

Note:

is considered to be an even index.

Input Format

The first line contains an integer,
(the number of test cases).
Each line of the subsequent lines contain a String,

.

Constraints

Output Format

For each String
(where ), print 's even-indexed characters, followed by a space, followed by

's odd-indexed characters.

Sample Input

2
Hacker
Rank

Sample Output

Hce akr
Rn ak

Explanation

Test Case 0:







The even indices are , , and , and the odd indices are , , and . We then print a single line of space-separated strings; the first string contains the ordered characters from 's even indices (), and the second string contains the ordered characters from 's odd indices (

).

Test Case 1:





The even indices are and , and the odd indices are and . We then print a single line of space-separated strings; the first string contains the ordered characters from 's even indices (), and the second string contains the ordered characters from 's odd indices ().
'''

words=list()
output=list()
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        words.append(input())
    for w in words:
        odd,even='',''
        for i in range(len(w)):
            if i%2==0:
                even+=w[i]
            else:
                odd+=w[i]
        output.append((even,odd))
    for even,odd in output:
        print(even,odd)