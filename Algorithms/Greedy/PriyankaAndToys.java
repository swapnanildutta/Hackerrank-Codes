/*
Link - https://www.hackerrank.com/challenges/priyanka-and-toys/problem

Priyanka works for an international toy company that ships by container. Her task is to the determine the lowest cost way to combine her orders for shipping. She has a list of item weights. The shipping company has a requirement that all items loaded in a container must weigh less than or equal to 4 units plus the weight of the minimum weight item. All items meeting that requirement will be shipped in one container.

What is the smallest number of containers that can be contracted to ship the items based on the given list of weights?

For example, there are items with weights . This can be broken into two containers:  and . Each container will contain items weighing within  units of the minimum weight item.

Function Description

Complete the toys function in the editor below. It should return the minimum number of containers required to ship.

toys has the following parameter(s):

w: an array of integers that represent the weights of each order to ship
Input Format

The first line contains an integer , the number of orders to ship.
The next line contains  space-separated integers, , representing the orders in a weight array.

Constraints



Output Format

Return the integer value of the number of containers Priyanka must contract to ship all of the toys.

Sample Input

8
1 2 3 21 7 12 14 21
Sample Output

4
Explanation

The first container holds items weighing ,  and . (weights in range )
The second container holds the items weighing  units. ()
The third container holds the item weighing  units. ()
The fourth container holds the items weighing  and  units. ()

 containers are required.
 */
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class PriyankaAndToys {

    static int toys(int[] w) {
    	Arrays.sort(w);    	
    	int idx=0;
//    	while(w[idx]==0){
//    		idx++;
//    	}
        int c=w[idx]+4;        
        int rv=1;

        for(int i=1;i<w.length;i++){
//        	if(w[i]==0){
//        		continue;
//        	}
            if(w[i]>c){
                c=w[i]+4;
                rv++;
            }
        }
        return rv;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] w = new int[n];
        for(int w_i = 0; w_i < n; w_i++){
            w[w_i] = in.nextInt();
        }
        int result = toys(w);
        System.out.println(result);
        in.close();
    }
}
