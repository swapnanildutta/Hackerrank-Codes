/* Print a pattern of numbers from  to  as shown below. Each of the numbers is separated by a single space.

                            4 4 4 4 4 4 4  
                            4 3 3 3 3 3 4   
                            4 3 2 2 2 3 4   
                            4 3 2 1 2 3 4   
                            4 3 2 2 2 3 4   
                            4 3 3 3 3 3 4   
                            4 4 4 4 4 4 4   
Input Format

The input will contain a single integer .

Constraints


Sample Input:

2
Sample Output:

2 2 2
2 1 2
2 2 2
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n,i,j,k;
    scanf("%d", &n);
    for(i=1;i<2*n;i++)
    {
        if(i<=n)
        {
            k=n;
            for(j=1;j<2*n;j++)
            {
                printf("%d ",k);
                if(i>j)
                k--;
                if(i+j>=2*n)
                k++;
                
            }
            printf("\n");
        }
        if(i>n)
        {
            k=n;
            for(j=1;j<2*n;j++)
            {
                printf("%d ",k);
                if(i+j<2*n)
                k--;
                if(j>=i)
                k++;
        
            }
            printf("\n");
        }
    }
  	// Complete the code to print the pattern.
    return 0;
}


