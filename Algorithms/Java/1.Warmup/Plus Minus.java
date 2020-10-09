import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        int size=in.nextInt();
        int[] array=new int[size];
        for(int i=0;i<size;i++)
            array[i]=in.nextInt();
        float min=0,zero=0,plus=0;
        for(int i=0;i<size;i++){
            if(array[i]>0)
                plus++;
            else if(array[i]==0)
                zero++;
            else
                min++;
        }
            min=min/size;
            plus=plus/size;
            zero=zero/size;
            System.out.println(String.format("%.3f",plus));
            System.out.println(String.format("%.3f",min));
            System.out.println(String.format("%.3f",zero));
    }
}
