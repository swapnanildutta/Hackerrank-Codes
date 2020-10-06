https://www.hackerrank.com/challenges/game-with-cells/problem
/*
Link = https://www.hackerrank.com/challenges/game-with-cells/problem

Problem Statement
Luke is daydreaming in Math class. He has a sheet of graph paper with n rows and m columns, 
and he imagines that there is an army base in each cell for a total of n*m bases. 
He wants to drop supplies at strategic points on the sheet, marking each drop point with a red dot. 
If a base contains at least one package inside or on top of its border fence, then it's considered to be supplied. For example:
Given n and m , what's the minimum number of packages that Luke must drop to supply all of his bases?

Example
n=2
m=3

Packages can be dropped at the corner between cells (0, 0), (0, 1), (1, 0) and (1, 1) to supply 4 bases. 
Another package can be dropped at a border between (0, 2) and (1, 2). This supplies all bases using 2 packages.

Sample Input 0

2 2
Sample Output 0

1
Explanation 0

Luke has four bases in a 2 x 2 grid. If he drops a single package where the walls of all four bases intersect, then those four cells can access the package
*/
import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    /*
     * Complete the gameWithCells function below.
     */
    static int gameWithCells(int n, int m) {
        /*
         * Write your code here.
         */
         return ((n + n%2) * (m + m%2))/4;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nm = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nm[0].trim());

        int m = Integer.parseInt(nm[1].trim());

        int result = gameWithCells(n, m);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();
    }
}
