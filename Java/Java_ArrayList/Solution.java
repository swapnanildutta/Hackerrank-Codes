/*Hackerrank Java Problem : Java ArrayList 
The idea is to create an array of ArrayList and answer the query in O(1) time.*/

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> al[] = new ArrayList[n];
        for(int i = 0 ; i < n ; i++)
        {
            int d = sc.nextInt();
            al[i] = new ArrayList<>();
            for(int j = 0; j < d; j++)
            {
                int val = sc.nextInt();
                al[i].add(val);
            }
    
        }
        int query = sc.nextInt();
        for(int i = 0 ; i < query ; i ++)
        {
            int x = sc.nextInt();
            int y = sc.nextInt();
            if( x < 1 || x > n)
             System.out.println("ERROR!");
             else if(al[x-1].size() < 1 || al[x-1].size() < y )
             System.out.println("ERROR!");
             else
             System.out.println(al[x-1].get(y-1));
             
        }
    }
}
