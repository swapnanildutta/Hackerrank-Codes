//Problem

//Given a string, , consisting of alphabets and digits, find the frequency of each digit in the given string.

// Input Format

// The first line contains a string,  which is the given number.

// Constraints


// All the elements of num are made of english alphabets and digits.

// Output Format

// Print ten space-separated integers in a single line denoting the frequency of each digit from  to .

// Sample Input 0

// a11472o5t6
// Sample Output 0

// 0 2 1 0 1 1 1 1 0 0 
// Explanation 0

// In the given string:

//  occurs two times.
//  and  occur one time each.
// The remaining digits  and  don't occur at all.
// Sample Input 1

// lw4n88j12n1
// Sample Output 1

// 0 2 1 0 1 0 0 0 2 0 
// Sample Input 2

// 1v88886l256338ar0ekk
// Sample Output 2

// 1 1 1 2 0 1 2 0 5 0 

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int i,n,ar[10]={0};
    char num[1000];
    scanf("%s",num);
    for(i=0;i<strlen(num);i++)
    {
        switch(num[i])
        {
            case '0':ar[0]++;break;
            case '1':ar[1]++;break;
            case '2':ar[2]++;break;
            case '3':ar[3]++;break;
            case '4':ar[4]++;break;
            case '5':ar[5]++;break;
            case '6':ar[6]++;break;
            case '7':ar[7]++;break;
            case '8':ar[8]++;break;
            case '9':ar[9]++;break;
            default : continue;
        }
    } 

    for(i=0;i<10;i++)
    {
        printf("%d ",ar[i]);
    }
    return 0;
}
