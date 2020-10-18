/* 
LINK = https://www.hackerrank.com/challenges/lowest-triangle/problem

Given integers b and a, find the smallest integer h, such that there exists a triangle of height h, base b, having an area of at least a.
                           _._
                  *         :
                 * *        height
                * * *       :
               * * * *      :
              * * * * *    _:_

Example
b = 4
a = 6

The minimum height h is 3 . One example is a triangle formed at points (0, 0), (4, 0), (2, 3).

Function Description

Complete the lowestTriangle function in the editor below.

lowestTriangle has the following parameters:

int b: the base of the triangle
int a: the minimum area of the triangle
Returns

int: the minimum integer height to form a triangle with an area of at least a
Input Format

There are two space-separated integers b and a, on a single line.

Constraints

Sample Input 0

2 2
Sample Output 0

2


*/
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int base, area, height, newarea;

    cin >> base >> area;    //taking input

    height = (area * 2) / base; //re-arranging the old famous formula of finding area of triangle as per our requirement

    newarea = height * base;

    if(newarea == (2*area))     //check whether the computated height sufficient to get given area or else add one more unit to it.
        cout << height  <<endl;
    else
        cout << height + 1 <<endl;
    return 0;
}
