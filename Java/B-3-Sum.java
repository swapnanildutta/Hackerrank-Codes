/*
Problem link :- https://www.hackerrank.com/contests/oa2021b2/challenges/b-3-sum


Given an array A[] of N numbers and another number x, determine whether or not there exist three elements in A[] whose sum is exactly x.

After you pass test cases on hacker rank, please pass all test cases here.

Use sliding window technique. Do this problem in o(n2)

Input Format

First line of input contains number of testcases T. For each testcase, first line of input contains n and x. Next line contains array elements.

Constraints

1 ≤ T ≤ 100 1 ≤ N ≤ 103 1 ≤ A[i] ≤ 105

Output Format

Print 1 if there exist three elements in A whose sum is exactly x, else 0.

Sample Input 0

2
6 13
1 4 45 6 10 8
5 10
1 2 4 3 6
Sample Output 0

1
1
*/

public class Solution {
   static int sum(int[]arr,int n,int sum){
       
       for(int i=0;i<n;i++){
           HashSet <Integer> s=new HashSet<Integer>();
           int curr_sum=sum-arr[i];
           for(int j=i+1;j<n;j++){
               if(s.contains(curr_sum-arr[j])){
                   return 1;
               }
               else{
                   s.add(arr[j]);
               }
           }
       }
       return 0;
   }
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
       Scanner s=new Scanner(System.in);
        int t=s.nextInt();
        for(int i=0;i<t;i++){
            int n=s.nextInt();
            int k=s.nextInt();
            int []arr=new int[n];
            for(int j=0;j<n;j++){
                arr[j]=s.nextInt();
            }
            System.out.println(sum(arr,n,k));
        }
            
        }
    }


