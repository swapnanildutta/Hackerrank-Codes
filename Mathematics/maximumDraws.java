/*
Problem Link = https://www.hackerrank.com/challenges/maximum-draws/problem

Problem Statement
A person is getting ready to leave and needs a pair of matching socks. If there are n colors of socks in the drawer, how many socks need to be removed to be certain of having a matching pair?

Example n=2
There are 2 colors of socks in the drawer. If they remove 2 socks, they may not match. The minimum number to insure success is 3.
Sample Input

2
1
2
Sample Output

2
3
Explanation
Case 1 : Only 1 color of sock is in the drawer. Any 2 will match.
Case 2 : 2 colors of socks are in the drawer. The first two removed may not match. At least 3 socks need to be removed to guarantee success.
*/
import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    /*
     * Complete the maximumDraws function below.
     */
    static int maximumDraws(int n) {
        /*
         * Write your code here.
         */
         if(n==0)
          return 0 ;
          else
           return (n+1);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = Integer.parseInt(scanner.nextLine().trim());

        for (int tItr = 0; tItr < t; tItr++) {
            int n = Integer.parseInt(scanner.nextLine().trim());

            int result = maximumDraws(n);

            bufferedWriter.write(String.valueOf(result));
            bufferedWriter.newLine();
        }

        bufferedWriter.close();
    }
}
