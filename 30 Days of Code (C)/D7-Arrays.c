/*
Objective
    Today, we're learning about the Array data structure. Check out the Tutorial tab for learning materials and an instructional video!
Task
    Given an array,    , of integers, print    's elements in reverse order as a single line of space-separated numbers.

Input Format
    The first line contains an integer,    (the size of our array).
    The second line contains space-separated integers describing array    's elements.

Constraints
                , where is the        integer in the array.

Output Format
    Print the elements of array in reverse order as a single line of space-separated numbers.

Sample Input
    4
    1 4 3 2

Sample Output
    2 3 4 1
*/


#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int n,i;
    scanf("%d",&n);
    int Arr[n];
    for(i = 0;i < n;i++)
    scanf("%d",&Arr[i]);
    for(i = n-1;i >= 0;i--)
    printf("%d ",Arr[i]);
}