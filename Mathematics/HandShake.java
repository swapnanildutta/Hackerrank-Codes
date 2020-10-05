/*
Link = https://www.hackerrank.com/challenges/handshake/problem

Probolem Statement
At the annual meeting of Board of Directors of Acme Inc. If everyone attending shakes hands exactly one time with every other attendee, how many handshakes are there?

Example
n=3

There are 3 attendees p1, p2 and p3. p1 shakes hands with p2 and p2 ,and p2 shakes hands with p3. Now they have all shaken hands after 3 handshakes.

Sample Input

2
1
2
Sample Output

0
1
Explanation

Case 1 : The lonely board member shakes no hands, hence 0.
Case 2 : There are 2 board members, so 1 handshake takes place.

*/

import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    /*
     * Complete the handshake function below.
     */
    static int handshake(int n) {
        /*
         * Write your code here.
         */
        return (n*(n-1))/ 2;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = Integer.parseInt(scanner.nextLine().trim());

        for (int tItr = 0; tItr < t; tItr++) {
            int n = Integer.parseInt(scanner.nextLine().trim());

            int result = handshake(n);

            bufferedWriter.write(String.valueOf(result));
            bufferedWriter.newLine();
        }

        bufferedWriter.close();
    }
}
