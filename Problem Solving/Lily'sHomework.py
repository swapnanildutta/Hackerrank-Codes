
"""
Whenever George asks Lily to hang out, she's busy doing homework. George wants to help her finish it faster, but he's in over his head! Can you help George understand Lily's homework so she can hang out with him?

Consider an array of  distinct integers, . George can swap any two elements of the array any number of times. An array is beautiful if the sum of  among  is minimal.

Given the array , determine and return the minimum number of swaps that should be performed in order to make the array beautiful.

For example, . One minimal array is . To get there, George performed the following swaps:

Swap      Result
      [7, 15, 12, 3]
3 7   [3, 15, 12, 7]
7 15  [3, 7, 12, 15]
It took  swaps to make the array beautiful. This is minimal among the choice of beautiful arrays possible.

Function Description

Complete the lilysHomework function in the editor below. It should return an integer that represents the minimum number of swaps required.

lilysHomework has the following parameter(s):

arr: an integer array
Input Format

The first line contains a single integer, , the number of elements in . The second line contains  space-separated integers .

Constraints

Output Format

Return the minimum number of swaps needed to make the array beautiful.

Sample Input

4
2 5 3 1
Sample Output

2
"""

try:
    raw_input
except NameError:
    raw_input = input

def solution(a):

    m = {}
    for i in range(len(a)):
        m[a[i]] = i 
        
    sorted_a = sorted(a)
    ret = 0
    
    for i in range(len(a)):
        if a[i] != sorted_a[i]:
            ret +=1
            
            ind_to_swap = m[ sorted_a[i] ]
            m[ a[i] ] = m[ sorted_a[i]]
            a[i],a[ind_to_swap] = sorted_a[i],a[i]
    return ret

raw_input()
a = [int(i) for i in raw_input().split(' ')]

asc=solution(list(a))
desc=solution(list(reversed(a)))
print (min(asc,desc))
