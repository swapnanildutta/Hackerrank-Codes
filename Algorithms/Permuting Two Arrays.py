'''# Problem: https://www.hackerrank.com/challenges/two-arrays/problem
# Score: 40
Consider two -element arrays of integers,  and . You want to permute them into some  and  such that the relation  holds for all  where . For example, if , , and , a valid  satisfying our relation would be  and ,  and .

You are given  queries consisting of , , and . For each query, print YES on a new line if some permutation ,  satisfying the relation above exists. Otherwise, print NO.

Function Description

Complete the twoArrays function in the editor below. It should return a string, either YES or NO.

twoArrays has the following parameter(s):

k: an integer
A: an array of integers
B: an array of integers
Input Format

The first line contains an integer , the number of queries.

The next  sets of  lines are as follows:

The first line contains two space-separated integers  and , the size of both arrays  and , and the relation variable.
The second line contains  space-separated integers .
The third line contains  space-separated integers .
Constraints

Output Format

For each query, print YES on a new line if valid permutations exist. Otherwise, print NO.

Sample Input

2
3 10
2 1 3
7 8 9
4 5
1 2 2 1
3 3 3 4
Sample Output

YES
NO
Explanation

We perform the following two queries:

, , and . We permute these into  and  so that the following statements are true:

Thus, we print YES on a new line.

, , and . To permute  and  into a valid  and , we would need at least three numbers in  to be greater than ; as this is not the case, we print NO on a new line.'''

n = int(input())
for _ in range(n):
    __, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())), reverse=True)
    if all([a[i] + b[i] >= k for i in range(len(a))]):
        print('YES')
    else:
        print('NO')
