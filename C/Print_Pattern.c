/*
Print a pattern of numbers from 1 to n as shown below. Each of the numbers is separated by a single space.

                            4 4 4 4 4 4 4  
                            4 3 3 3 3 3 4   
                            4 3 2 2 2 3 4   
                            4 3 2 1 2 3 4   
                            4 3 2 2 2 3 4   
                            4 3 3 3 3 3 4   
                            4 4 4 4 4 4 4   

Input Format

The input will contain a single integer n.

Constraints

1 <= n <= 1000

Sample Input 0

2

Sample Output 0

2 2 2
2 1 2
2 2 2

Sample Input 1

5

Sample Output 1

5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5

Sample Input 2

7

Sample Output 2

7 7 7 7 7 7 7 7 7 7 7 7 7 
7 6 6 6 6 6 6 6 6 6 6 6 7 
7 6 5 5 5 5 5 5 5 5 5 6 7 
7 6 5 4 4 4 4 4 4 4 5 6 7 
7 6 5 4 3 3 3 3 3 4 5 6 7 
7 6 5 4 3 2 2 2 3 4 5 6 7 
7 6 5 4 3 2 1 2 3 4 5 6 7 
7 6 5 4 3 2 2 2 3 4 5 6 7 
7 6 5 4 3 3 3 3 3 4 5 6 7 
7 6 5 4 4 4 4 4 4 4 5 6 7 
7 6 5 5 5 5 5 5 5 5 5 6 7 
7 6 6 6 6 6 6 6 6 6 6 6 7 
7 7 7 7 7 7 7 7 7 7 7 7 7 

*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n;
    scanf("%d", &n);
  	// Complete the code to print the pattern.
    int base = 1 + (2*(n-1));
    int initial, last;
    initial = 0;
    last = base;
    int i, x = n;
    while(x >= 1)
    {
        i = n;
        while(i != x)
        {
            printf("%d ", i);
            i--;
        }
        for(i = initial; i < last; i++)
        {
            printf("%d ", x);
        }
        i = x;
        while(i != n)
        {
            printf("%d ", i+1);
            i++;
        }
        printf("\n");
        initial += 1;
        last -= 1;
        x -= 1;
    }
    initial = last = base/2;
    x = 2;
    int count = 0;
    while(x <= n)
    {
        i = 0;
        int j;
        j = n;
        while(i != initial)
        {
            printf("%d ", j);
            i++;
            j--;
        }
        for(i = 0; i <= count; i++)
        {
            printf("%d ", x);
        }
        i = last;
        j = x;
        while(i != 0)
        {
            printf("%d ", j);
            j++;
            i--;
        }
        count += 2;
        initial -= 1;
        last -= 1;
        x += 1;
        printf("\n");

    }
    return 0;
}
