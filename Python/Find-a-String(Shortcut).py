'''
The user enters a string and a substring. We need to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
String letters are case-sensitive.

Input Format:
The first line of input contains the original string. The next line contains the substring.
Constraints:
Each character in the string is an ascii character.
Output Format:
Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input
AB CD EFABA
AB 
Sample Output
2
'''

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = string.count(sub_string)
    print(count)