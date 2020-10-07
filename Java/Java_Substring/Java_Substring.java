/*

Given a string S, and two indices,start and end, print a substring consisting of all characters in the inclusive range from start to end-1

Input Format

The first line contains a single string denoting s.
The second line contains two space-separated integers denoting the respective values of start and end

Output Format
Print the substring in the inclusive range from start to end-1.

Sample Input
Helloworld
3 7
-----------------
Sample Output

lowo


*/
import java.util.Scanner;
public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String S = in.next();
        int start = in.nextInt();
        int end = in.nextInt();
System.out.println(S.substring(start,end));
    }
}
