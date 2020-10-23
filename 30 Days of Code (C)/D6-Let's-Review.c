/*
Objective
    Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops. Check out the Tutorial tab for learning materials and an instructional video!

Task
    Given a string,   ,    of length that is indexed from to , print its even-indexed and odd-indexed characters as space-separated strings on a single line (see the Sample below for more detail).

Note: is considered to be an even index.

Input Format
    The first line contains an integer,    (the number of test cases).
    Each line of the subsequent lines contain a String,     .

Constraints

Output Format
    For each String    (where ), print 's even-indexed characters, followed by a space, followed by    's odd-indexed characters.

Sample Input
    2
    Hacker
    Rank

Sample Output
    Hce akr
    Rn ak

Explanation

Test Case 0:
    The even indices are , , and , and the odd indices are , , and . We then print a single line of space-separated strings; the first string contains the ordered characters from 's even indices (), and the second string contains the ordered characters from 's odd indices (   ).

Test Case 1:
    The even indices are and , and the odd indices are and . We then print a single line of space-separated strings; the first string contains the ordered characters from 's even indices (), and the second string contains the ordered characters from 's odd indices ().
*/
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void worker(){
    int i = 0;
    char string[10000];
    scanf("%s",&string);
    char even[5000], odd[5000];
    for(i; i < strlen(string) ; i++){
        if(i % 2 == 0)
            even[i/2] = string[i];
        else
            odd[(i - 1) / 2] = string[i];
    }
    printf("%s %s \n",even,odd);
}


int main() {
    int t; //for test cases
    scanf("%d",&t);
    while(t > 0){
        worker();
        t--;
    } 
    return 0;
}