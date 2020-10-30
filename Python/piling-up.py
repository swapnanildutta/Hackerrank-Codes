
'''

Piling Up!
https://www.hackerrank.com/challenges/piling-up/problem

There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if cube(i) is on top of cube(j) then sideLength(j) >= sideLength(i).

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.

Input Format

The first line contains a single integer T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains , the number of cubes.
The second line contains n space separated integers, denoting the sideLengths of each cube in that order.

Constraints
1 <= T <= 5
1 <= n <= 10^5
1 <= sideLength <= 2^31

Output Format

For each test case, output a single line containing either "Yes" or "No" without the quotes.

Sample Input

2
6
4 3 2 1 3 4
3
1 3 2

Sample Output

Yes
No

Explanation

In the first test case, pick in this order: left - 4, right - 4, left - 3, right - 3, left - 2, right - 1.
In the second test case, no order gives an appropriate arrangement of vertical cubes. 3 will always come after either 1 or 2.

'''

def clean_inputs(inpt, allowed_chars=[]):
    ret = ""
    for c in inpt:
        if c.isdigit() or c in allowed_chars:
            ret += c
    return ret

test_cases = int(clean_inputs(input()))

for i in range(test_cases):
    no_cubes = int(clean_inputs(input()))
    cubes = clean_inputs(input().strip(), [" "]).split(" ")
    for i in range(len(cubes)):
        cubes[i] = int(cubes[i])
    stack = []
    res = "Yes"
    while (len(cubes) > 0):
        if cubes[0] > cubes[-1]:
            li = 0
        else:
            li = -1
        if len(stack) == 0 or cubes[li] <= stack[-1]:
            stack.append(cubes.pop(li))
        else:
            res = "No"
            break
    print(res)
