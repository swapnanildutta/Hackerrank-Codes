'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

Input Format

A single line containing a string

.

Constraints

Output Format

Print the modified string

.

Sample Input 0

HackerRank.com presents "Pythonist 2".

Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".


'''
#Old Code

# def swap_case(s):
#     result=''
#     for i in s:
#         if i.isalpha() and i.isupper():
#             result+=i.lower()
#         elif i.isalpha() and i.islower():
#             result+=i.upper()
#         else:
#             result+=i
#     return result

def swap_case(s):
    s=s.swapcase()
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
