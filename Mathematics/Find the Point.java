/*
link = https://www.hackerrank.com/challenges/find-point/problem
Find the Point
Consider two points , p = (px,py) and q= (qx , qy). We consider the inversion or point reflection,r = (rx,ry),
of point p across point q to be a 180 rotation of point p around q.
Given n sets of points p and q , find r for each pair of points and print two space-separated integers
denoting the respective values of rx and ry on a new line.
Input Format
The first line contains an integer, , denoting the number of sets of points.
Each of the subsequent lines contains four space-separated integers describing the respective values of
, , , and defining points and .
Constraints
Output Format
For each pair of points and , print the corresponding respective values of and as two spaceseparated integers on a new line.
Sample Input
2
0 0 1 1
1 1 2 2
Sample Output
2 2
3 3
Explanation
The graphs below depict points , , and for the points given as Sample Input:
1.
Thus, we print and as 2 2 on a new line.
2.
Thus, we print and as 3 3 on a new line.
*/

import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    /*
     * Complete the findPoint function below.
     */
    static int[] findPoint(int px, int py, int qx, int qy) {
        /*
         * Write your code here.
         */
         int[] arr = new int[2];
         arr[0] = (2*qx - px);
         arr[1] = (2*qy - py);
       return arr; 
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(scanner.nextLine().trim());

        for (int nItr = 0; nItr < n; nItr++) {
            String[] pxPyQxQy = scanner.nextLine().split(" ");

            int px = Integer.parseInt(pxPyQxQy[0].trim());

            int py = Integer.parseInt(pxPyQxQy[1].trim());

            int qx = Integer.parseInt(pxPyQxQy[2].trim());

            int qy = Integer.parseInt(pxPyQxQy[3].trim());

            int[] result = findPoint(px, py, qx, qy);

            for (int resultItr = 0; resultItr < result.length; resultItr++) {
                bufferedWriter.write(String.valueOf(result[resultItr]));

                if (resultItr != result.length - 1) {
                    bufferedWriter.write(" ");
                }
            }

            bufferedWriter.newLine();
        }

        bufferedWriter.close();
    }
}
