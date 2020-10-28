/*
PROBLEM STATEMENT

Lilah has a string, , of lowercase English letters that she repeated infinitely many times.
Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.
For example, if the string  and , the substring we consider is , the first  characters of her infinite string. There are  occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length  
in the infinitely repeating string.
repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider

Input Format

The first line contains a single string, .
The second line contains an integer, .

Constraints:

1<= |s| <=100
1 <= |n| <= 10^12
For 25% of the test cases, n <= 10^6.

Output Format

Print a single integer denoting the number of letter a's in the first  letters of the infinite string created by repeating  infinitely many times.

Sample Input 0

aba
10
Sample Output 0

7
Explanation 0
The first  letters of the infinite string are abaabaabaa. Because there are  a's, we print  on a new line.

Sample Input 1

a
1000000000000
Sample Output 1

1000000000000
Explanation 1
Because all of the first  letters of the infinite string are a, we print  on a new line.
*/


#include <stdio.h>
#include <string.h>


int main( void ) {
    char s[1000];
    long long n;
    
    scanf("%s %lld", s, &n);
    
    int m = strlen(s);
    
    long long count = 0;
    for( int i = 0; i < m; i++ ) {
        if( s[i] == 'a' ) count++;
    }
    
    count *= n / m;
    
    for( int i = 0; i < n % m; i++ ) {
        if( s[i] == 'a' ) count++;
    }
    
    printf("%lld\n", count);
    
    return 0;
}
