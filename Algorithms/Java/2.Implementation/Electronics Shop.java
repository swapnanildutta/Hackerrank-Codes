import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        String[] bnm = scanner.nextLine().split(" ");

        int b = Integer.parseInt(bnm[0]);
        int n = Integer.parseInt(bnm[1]);
        int m = Integer.parseInt(bnm[2]);
        int[] keyboards = new int[n];
        String[] keyboardsItems = scanner.nextLine().split(" ");
        for (int keyboardsItr = 0; keyboardsItr < n; keyboardsItr++) {
            int keyboardsItem = Integer.parseInt(keyboardsItems[keyboardsItr]);
            keyboards[keyboardsItr] = keyboardsItem;
        }
        int[] drives = new int[m];
        String[] drivesItems = scanner.nextLine().split(" ");
        for (int drivesItr = 0; drivesItr < m; drivesItr++) {
            int drivesItem = Integer.parseInt(drivesItems[drivesItr]);
            drives[drivesItr] = drivesItem;
        }
        int max = -1;
        for(int i = 0 ; i < keyboards.length ; i++) {
            for(int j = 0 ; j < drives.length ; j++){
                int val = keyboards[i] + drives[j] ;
                if (val > max && val <= b){
                    max = val;
                }
            }
        }

        /*
        Alternate solution
        
        Arrays.sort(keyboards);
        Arrays.sort(drives);
        int max = -1;
        for(int i = keyboards.length - 1 ; i >= 0  ; i--) {
            for(int j = drives.length - 1 ; j >= 0 ; j--){
                int val = keyboards[i] + drives[j] ;
                if (val > max && val <= b){
                    max = val;
                    break;
                }
            }
        }
         */
        System.out.println(max);
    }
}
