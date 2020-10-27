'''
Debugging/Smart Number
Language: Python 3
Link: https://www.hackerrank.com/challenges/smart-number/problem
In this challenge, the task is to debug the existing code to successfully execute all provided test files.

A number is called a smart number if it has an odd number of factors. Given some numbers, find whether they are smart numbers or not.

Debug the given function is_smart_number to correctly check if a given number is a smart number.

Note: You can modify only one line in the given code and you cannot add or remove any new lines.

To restore the original code in the editor, create a new buffer by clicking on the top left icon in the editor.

Input Format

The first line of the input contains , the number of test cases.
The next  lines contain one integer each.

Constraints

, where  is the  integer.
Output Format

The output should consist of  lines. In the  line print YES if the  integer has an odd number of factors, else print NO.

Sample Input

4
1
2
7
169
Sample Output

YES
NO
NO
YES
Explanation

The factors of 1 are just 1 itself.So the answer is YES. The factors of 2 are 1 and 2.It has even number of factors.The answer is NO. The factors of 7 are 1 and 7.It has even number of factors.The answer is NO. The factors of 169 are 1,13 and 169.It has odd number of factors.The answer is YES.
'''

# Odd number of factors means squared numbers.
# Change 'if num / val == 1:' to 'if num / val == val:'

import math

def is_smart_number(num):
    val = int(math.sqrt(num))
    
    if num / val == val:
        return True
    return False

for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")



