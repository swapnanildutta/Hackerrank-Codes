import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        
        int sp = n - 1;
        int st = 1;
        for(int i = 0 ; i < n ; i++){
            for(int j = 0 ; j < sp ; j++){
                System.out.print(" ");
            }
            for(int j = 0 ; j < st ; j++){
                System.out.print("#");
            }
            sp--;
            st++;
            System.out.println();
        }

    }
}
