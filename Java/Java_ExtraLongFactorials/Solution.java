/*
https://www.hackerrank.com/challenges/extra-long-factorials/

The factorial of the integer n, written n!, is defined as:
n! = n*(n-1)*(n-2)*...*3*2*1

Calculate and print the factorial of a given integer.

For example, if n=30, we calculate 30*29*28*...*2*1 and get 265252859812191058636308480000000.


Function Description
Complete the extraLongFactorials function in the editor below. It should print the result and return.

extraLongFactorials has the following parameter(s):
- n: an integer
Note: Factorials of n>20 can't be stored even in a 64-bit long long variable. Big integers must be used for such calculations. Languages like Java, Python, Ruby etc. can handle big integers, but we need to write additional code in C/C++ to handle huge values.

We recommend solving this challenge using BigIntegers.


Input Format
Input consists of a single integer n


Constraints
1<=n<=100


Output Format
Print the factorial of n.


Sample Input
25

Sample Output
15511210043330985984000000

Explanation
25! = 25*24*23*...*3*2*1

 */

package Java_ExtraLongFactorials;
import java.math.BigInteger;
import java.util.Scanner;

public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    static BigInteger extraLongFactorials(BigInteger n) {
        if (n.intValue() == 1 || n.intValue() == 0)
            return new BigInteger("1");

        return n.multiply(extraLongFactorials(new BigInteger(String.valueOf(n.intValue() - 1))));
    }

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        System.out.print(extraLongFactorials(new BigInteger(String.valueOf(n))));

        scanner.close();
    }

}