QUESTION LINK: https://www.hackerrank.com/challenges/java-string-compare/problem
SOLUTION IN JAVA
import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";
        int n=s.length();
        int i;//loop control variable
        String arr[]=new String[n*k];
        int j=0;//for arr
        for(i=0;i<n;i++)
        {
            if(i+k<=n)
            {
                 arr[j]=s.substring(i,i+k);
                 j++;
            }
        }
        for(int k1 = 0; k1<j-1; k1++) {
         for (int k2 = k1+1; k2<j; k2++) {
            if(arr[k1].compareTo(arr[k2])>0) {
               String temp = arr[k1];
               arr[k1] = arr[k2];
               arr[k2] = temp;
            }
         }
      }
        smallest=arr[0];
        largest=arr[j-1];
        return smallest + "\n" + largest;
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}
