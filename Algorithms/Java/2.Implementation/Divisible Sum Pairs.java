import java.io.*;
import java.util.*;

public class Solution {
public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int a[] = new int[k];
        int count = 0;
        for(int a_i=0; a_i < n; a_i++){
            int number = in.nextInt();
            number = number % k;
            int complement = number == 0 ? k : number;
            count += a[k-complement];
            a[number] += 1;
        }
        System.out.println(count);
    }
}
