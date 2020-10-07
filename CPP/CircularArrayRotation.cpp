/*
Circular Array Rotation:

For each array, perform a number of right circular rotations and return the value of the element at a given index.
For example, array a=[3,4,5] , number of rotations, k=2  and indices to check, m=[1,2] .
First we perform the two rotations:
[3,4,5] -> [5,3,4] -> [4,5,3]

Now return the values from the zero-based indices 1 and 2 as indicated in the m array.
a[1] = 5
a[2] = 3

Function Description

Complete the circularArrayRotation function in the editor below. It should return an array of integers representing the values at the specified indices.

circularArrayRotation has the following parameter(s):

- a: an array of integers to rotate
- k: an integer, the rotation count
-queries: an array of integers, the indices to report

Input Format

The first line contains 3 space-separated integers,n ,k  and q , the number of elements in the integer array, the rotation count and the number of queries.
The second line contains n space-separated integers, where each integer i describes array element a[i] (where 0 <= i < n).
Each of the q subsequent lines contains a single integer denoting m, the index of the element to return from a.

Output Format

For each query, print the value of the element at index  of the rotated array on a new line.

Sample Input 0

3 2 3
1 2 3
0
1
2
Sample Output 0

2
3
1
Explanation 0

After the first rotation, the array becomes [3,1,2].
After the second (and final) rotation, the array becomes [2,3,1].

Let's refer to the array's final state as array b=[2,3,1]. For each query, we just have to print the value of b(m) on a new line:

1) m=0, b(0)=2.
2) m=1, b(1)=3.
3) m=2, b(2)=1.

*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, k, q;
    scanf("%d", &n);
    scanf("%d", &k);
    scanf("%d", &q);
    int data[n];
    for (int i = 0; i < n; i++)
        scanf("%d", &data[i]);
    k = k % n;
    while (q--)
    {
        int x;
        scanf("%d", &x);
        x = x - k;
        if (x < 0)
            x = x + n;
        printf("%d\n", data[x]);
    }
    return 0;
}