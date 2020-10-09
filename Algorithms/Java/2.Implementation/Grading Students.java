import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for(int a0 = 0; a0 < n; a0++){
            int grade = in.nextInt();
            if (grade >= 38) {
                if (grade % 5 >= 3) {
                    grade += 5 - (grade % 5);
                }
            }
            System.out.println(grade);
        }
    }
}