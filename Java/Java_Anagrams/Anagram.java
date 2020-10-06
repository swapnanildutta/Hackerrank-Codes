/* Two strings,  and , are called anagrams if they contain all the same characters in the same frequencies. For example, the anagrams of CAT are CAT, ACT, TAC, TCA, ATC, and CTA.

Complete the function in the editor. If  and  are case-insensitive anagrams, print "Anagrams"; otherwise, print "Not Anagrams" instead.

Input Format

The first line contains a string denoting .
The second line contains a string denoting .

Constraints

Strings  and  consist of English alphabetic characters.
The comparison should NOT be case sensitive.
Output Format

Print "Anagrams" if  and  are case-insensitive anagrams of each other; otherwise, print "Not Anagrams" instead.

Sample Input 0

anagram
margana
Sample Output 0

Anagrams
*/

package Java_Anagrams;

import java.util.Scanner;

public class Anagram {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }

    static boolean isAnagram(String a, String b) {

        // Declarations
        int aLength = a.length();
        int bLength = b.length();
        int anagramLength = aLength < 25 ? aLength :25;
        int[] anagram = new int[anagramLength];

        // Check constraints
        if (aLength < 1 || aLength > 50) return false;
        if (bLength != aLength) return false;

        // Convert strings to same case
        a = a.toLowerCase();
        b = b.toLowerCase();

        // Increment / decrement counter for respective element
        for (int i = 0; i < aLength; i++) {
            anagram[(((int) a.charAt(i)) - 97) % aLength]++;
            anagram[(((int) b.charAt(i)) - 97) % aLength]--;
        }

        // Search for counter not equal to 0
        for (int i = 0; i < anagram.length; i++) {
            if (anagram[i] != 0) return false;
        }

        return true;
    }
}
