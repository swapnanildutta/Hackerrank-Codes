#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int i,j,start,end,q,a,count=0,count1=0;
    long long int square,square1;
    scanf("%d %d",&start,&end);
    for(i=start;i<=end;i++)
    {
        count1 = 0;
        square = pow(i,2);
        square1 = square;
        while (square1 != 0) 
        {
        square1 /= 10;     
        count1++;
        }
        j = (count1/2);
        if( count1%2 == 0)
        {q = square % (int)pow(10,j);
        a = (int)(square/(int)pow(10,j)) ;
        if( a + q == i && q != 0)
        {
            printf("%d ",i);
            count++;
        }
        }
        if(count1%2 != 0)
        {
            q = square % (int)pow(10,j+1);
            a = (int)(square/(int)pow(10,j+1)) ;
        if( a + q == i && q != 0)
        {
            printf("%d ",i);
            count++;
        }
        }
    }
    if(count == 0)
    {
        printf("INVALID RANGE");
    }
    return 0;
}
