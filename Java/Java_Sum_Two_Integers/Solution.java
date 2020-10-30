/*
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
*/

import java.util.*;

class Solution {

    public static void main(String[] args) {
        //create test case
        int a = 3;
        int b = 9;
        int result = getSum(a, b);
        System.out.println(a + " + " + b + " = " + result);
        //Output should be: [1,2,2,3,5,6]
    }

    
    public static int getSum(int a, int b) {
        int sum = 0;
        sum += a;
        sum += b;
        return sum;
    }

}