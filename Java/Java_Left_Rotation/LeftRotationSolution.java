/* 

Left Rotation Hackerrank Problem
https://www.hackerrank.com/challenges/array-left-rotation/problem

Problem: A left rotation operation on an array of size  shifts each of the array's elements  unit to the left. Given an integer, , rotate the array that many steps left and return the result.

Example
d = 2
arr = [1,2,3,4,5]
After 2 rotations, arr' = [3,4,5,1,2] .

Function Description

Complete the rotateLeft function in the editor below.
rotateLeft has the following parameters:
-int d: the amount to rotate by
-int arr[n]: the array to rotate

Returns

-int[n]: the rotated array

Input Format

The first line contains two space-separated integers that denote , the number of integers, and , the number of left rotations to perform.

The second line contains  space-separated integers that describe .

Constraints

1 <= n <= 10^5
1 <= d <= n
1 <= a[i] <= 10^6

Sample Input

5 4
1 2 3 4 5

Sample Output

5 1 2 3 4

Explanation

To perform  left rotations, the array undergoes the following sequence of changes:
[1,2,3,4,5] --> [2,3,4,5,1]  --> [3,4,5,1,2] --> [4,5,1,2,3] --> [5,1,2,3,4]

*/


import java.util.*;

package mypackage;

public class LeftRotationSolution {


    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        String[] nd = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nd[0]);

        int d = Integer.parseInt(nd[1]);

        int[] a = new int[n];

        String[] aItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int aItem = Integer.parseInt(aItems[i]);
            a[i] = aItem;
        }
        int[] rotated= new int[n];
        for(int i=0,pos=n-d;i<n;i++){
            rotated[pos]=a[i];
            pos++;
            if(pos==n)pos=0;
        }
        for(int i=0;i<n;i++)System.out.print(rotated[i]+" ");
        scanner.close();
    }
  
}
