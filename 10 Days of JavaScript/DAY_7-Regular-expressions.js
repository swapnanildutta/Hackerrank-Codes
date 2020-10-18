/*DAY-7*/
/*Objective

In this challenge, we use a Regular Expression to evaluate a string. Check out the attached tutorial for more details.

Task

Complete the function in the editor below by returning a RegExp object, , that matches any string  that begins and ends with the same vowel. Recall that the English vowels are a, e, i, o, and u.

Constraints

The length of string  is  .
String  consists of lowercase letters only (i.e., [a-z]).
Output Format

The function must return a RegExp object that matches any string  beginning with and ending in the same vowel.

Sample Input 0

bcd
Sample Output 0

false
Explanation 0

This string starts with (and ends in) a consonant, so it cannot start and end with the same vowel.

Sample Input 1

abcd
Sample Output 1

false
Explanation 1

This string ends in a consonant, so it cannot start and end with the same vowel.

Sample Input 2

abcda
Sample Output 2

true
Explanation 2

This string starts and ends with the same vowel (a).

Sample Input 3

abcdo
Sample Output 3

false
Explanation 3

This string starts with the vowel a but ends in the vowel o.
*/

/*SOLUTION*/



function regexVar() {
    /*
     * Declare a RegExp object variable named 're'
     * It must match a string that starts and ends with the same vowel (i.e., {a, e, i, o, u})
     */
    const re = /^([a,e,i,o,u]).*\1$/;
    
    
    /*
     * Do not remove the return statement
     */
    return re;
}


