/*
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?

 

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false
 

Constraints:

-231 <= x <= 231 - 1
*/

class Solution {
  public static void main(String[] args) {
    //create randome test case
    int number = 10;
    System.out.println("Check if " + number + " is palindrome: " + isPalindrome(number));

    int numberPalindrome = 11;
    System.out.println("Check if " + numberPalindrome + " is palindrome: " + isPalindrome(numberPalindrome));
  }

  public static boolean isPalindrome(int x) {
    int reverse = 0;
    int checkx = x;
    while (checkx != 0) {
        reverse = reverse * 10 + checkx % 10;
        checkx = checkx / 10;
    }
    if (reverse == x && x < 0) {
        return false;
    }
    else if (reverse == x && x >= 0) {
        return true;
    }
    return false;
  }
}