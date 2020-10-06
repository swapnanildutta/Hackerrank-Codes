/*A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.(Wikipedia)
-----------------------------------------------------------------------------------
Given a string "A", print Yes if it is a palindrome, print No otherwise.
-----------------------------------------------------------------------------------
Constraints

"A" string will consist at most 50 lower case english letters.
-------------------------------------------------------------------------------------
Sample Input
madam

Sample Output
Yes

*/





import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 Scanner sc=new Scanner(System.in);
	        String A=sc.next();
	        
	       StringBuilder sb=new StringBuilder(A);
	       StringBuilder rev=sb.reverse();
	       String reverseString=new String(rev);
	      
	       if(A.equals(reverseString) ){
	    	   System.out.println("yes");
	       }
	       else {
	    	   System.out.println("no");
	       }
	       
	       
	       
		}
	}



