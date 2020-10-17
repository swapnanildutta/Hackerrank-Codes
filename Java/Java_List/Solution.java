/*Hackerrank Java Problem : Java List 
Problem Statement : 
For this problem, we have 2 types of queries you can perform on a List:
1. Insert y at index x:
Insert
x y
2. Delete the element at index x:
Delete
x

Given a list,L , of N integers, perform Q queries on the list. Once all queries are completed, print the modified list as a single line of space-separated integers.
Input Format : 
The first line contains an integer, N (the initial number of elements in L).
The second line contains N space-separated integers describing L.
The third line contains an integer, Q (the number of queries).
The 2Q subsequent lines describe the queries, and each query is described over two lines:

If the first line of a query contains the String Insert, then the second line contains two space separated integers x y, and the value y must be inserted into L at index x.
If the first line of a query contains the String Delete, then the second line contains index x, whose element must be deleted from L.
Constraints :
1 <= N <= 4000
1 <= Q <= 4000
Each element in is a 32-bit integer.
*/
import java.io.*;
import java.util.*;

public class Solution 
{

    public static void main(String[] args) 
    {
        Scanner sc=new Scanner(System.in);
        int N = sc.nextInt();
        List L = new ArrayList<Integer>();
        for (int i = 0; i < N; i++)
        {
            L.add(sc.nextInt());
        }
        int Q = sc.nextInt();
        for (int q = 0; q < Q; q++)
        {
            String Z;
            Z = sc.next();
            if (Z.equals("Insert"))
            {
                L.add(sc.nextInt(),sc.nextInt());
            }
            else 
            {
                L.remove(sc.nextInt());
            }
        }
        for(int i = 0; i <L.size(); i++) 
        {   
            System.out.print(L.get(i) + " ");
        }  

    }
}