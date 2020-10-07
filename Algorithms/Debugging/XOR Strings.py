'''
Debugging/XOR Strings
Language: Python 3
Link: https://www.hackerrank.com/challenges/strings-xor/problem

In this challenge, the task is to debug the existing code to successfully execute all provided test files.

Given two strings consisting of digits 0 and 1 only, find the XOR of the two strings.

To know more about XOR Click Here

Debug the given function strings_xor to find the XOR of the two given strings appropriately.

Note: You can modify at most three lines in the given code and you cannot add or remove lines to the code.

To restore the original code in the editor, create a new buffer by clicking on the top left icon in the editor.

Input Format

The input consists of two lines. The first line of the input contains the first string, , and the second line contains the second string, .

Constraints

Output Format

Print the string obtained by the XOR of the two input strings in a single line.

Sample Input

10101
00101
Sample Output

10000
Explanation

The XOR of the two strings  and  is .
'''

# Change = to ==

def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0';
        else:
            res += '1';
    return res

s = input()
t = input()
print(strings_xor(s, t))

