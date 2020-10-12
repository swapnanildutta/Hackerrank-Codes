'''Alice has a binary string. She thinks a binary string is beautiful if and only if it doesnt contain the substring.

In one step, Alice can change a  to a  or vice versa. Count and print the minimum number of steps needed to make Alice see the string as beautiful.

For example, if Alices string is  she can change any one element and have a beautiful string.

Function Description: Complete the beautifulBinaryString function in the editor below. It should return an integer representing the minimum moves required.

beautifulBinaryString has the following parameter(s):
b: a string of binary digits

Input Format
The first line contains an integer , the length of binary string.
The second line contains a single binary string .

Constraints
1 <= n <= 100
b[i] E {0,1}

Output Format
Print the minimum number of steps needed to make the string beautiful.

Sample Input 1
5
01100
Sample Output 1
0

Sample Case 1:
In this sample b="01100"
Explanation 1
The substring "010" does not occur in b, so the string is already beautiful and we print 0.

'''

#!/bin/python3

import os

# Complete the beautifulBinaryString function below.

def beautifulBinaryString(b):
    subs="010"
    change=0
    i=0
    while i < len(b):
        i+=1
        if b.find(subs) == -1 :
            return change
        else:
            ind=b.index(subs)
            print(ind)
            s=[]
            for ab in b:
                s.append(ab)
            s[ind+2]='1'
            change+=1
            print(s)
            b=""
            for ele in s:
                b+=ele
    return 2
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
