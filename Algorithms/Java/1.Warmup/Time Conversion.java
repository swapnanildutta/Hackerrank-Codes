import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        String timeIn = in.next();
        if(timeIn.endsWith("PM") && !timeIn.substring(0,2).equals("12")) {
            int hrs = 12 + Integer.parseInt(timeIn.substring(0,2));
            String rem = timeIn.substring(2,8);
            System.out.println(hrs + rem);
        }
        else {
            if(timeIn.substring(0,2).equals("12") && timeIn.endsWith("AM")) {
                String hrs = "00";
                String rem = timeIn.substring(2,8);
                System.out.println(hrs + rem);
            }
            else
                System.out.println(timeIn.substring(0,8));
        }
    }
}