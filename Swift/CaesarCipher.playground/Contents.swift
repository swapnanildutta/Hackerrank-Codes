//Problem Caesar Chiper
// https://www.hackerrank.com/challenges/caesar-cipher-1/problem
/*
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

 Original alphabet:      abcdefghijklmnopqrstuvwxyz
 Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
 
 For example, the given cleartext s=There's-a-starman-waiting-in-the-sky and the alphabet is rotated by k=3. The encrypted string is Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb.

 Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

 Function Description

 Complete the caesarCipher function in the editor below. It should return the encrypted string.

 caesarCipher has the following parameter(s):

 s: a string in cleartext
 k: an integer, the alphabet rotation factor
 Input Format

 The first line contains the integer, , the length of the unencrypted string.
 The second line contains the unencrypted string, .
 The third line contains , the number of letters to rotate the alphabet by.

 Constraints

 1 <= n <= 100
 0 <= k <= 100


  is a valid ASCII string without any spaces.

 Output Format

 For each test case, print the encoded string.

 Sample Input

 11
 middle-Outz
 2
 Sample Output

 okffng-Qwvb
 Explanation

 Original alphabet:      abcdefghijklmnopqrstuvwxyz
 Alphabet rotated +2:    cdefghijklmnopqrstuvwxyzab

 m -> o
 i -> k
 d -> f
 d -> f
 l -> n
 e -> g
 -    -
 O -> Q
 u -> w
 t -> v
 z -> b

*/

func encryptInput(input: String, rotation: Int) -> String {
    var encryptedString = String()
    for char in input.unicodeScalars {
        var code = Int(char.value)
        // is lowercased letter
        if (97...122).contains(char.value) {
            code += rotation
            while code > 122 {
                // reduce until in char range
                code -= (122 - 96)
            }
        // is uppercased letter
        } else if (65...90).contains(char.value) {
            code += rotation
            while code > 90 {
                // reduce until in char range
                code -= (90 - 64)
            }
        }
        encryptedString += String(Character(UnicodeScalar(code)!))
    }
    return encryptedString
}

encryptInput(input: "hola", rotation: 1)
