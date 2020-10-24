//Small Triangles, Large Triangles
//All test cases passed
/*
You are given n triangles, specifically, their sides a,b  and c . Print them in the same style but sorted by their areas from the smallest one to the largest one. It is guaranteed that all the areas are different.

The best way to calculate a volume of the triangle with sides a,b and c is Heron's formula.

Input Format

First line of each test file contains a single integer n. n lines follow with a, b and c on each separated by single spaces.

Constraints
1<=n<=100
1<=a,b,c<=70
a+b>c,a+c>b, and b+c>a

Output Format

Print exactly n lines. On each line print 3 integers separated by single spaces, which are a, b and c of the corresponding triangle.

Sample Input 0

3
7 24 25
5 12 13
3 4 5

Sample Output 0

3 4 5
5 12 13
7 24 25

Explanation 0

The square of the first triangle is . The square of the second triangle is . The square of the third triangle is . So the sorted order is the reverse one.
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;

float area(int a,int b,int c)
{
    float p,ar;
    p=(a+b+c)/2.0;
    ar = p*(p-a)*(p-b)*(p-c);
    return ar;
}

//Sort all triangles in ascending order of the area
void sort_by_area(triangle* tr, int n) {
    triangle temp;
    int i,j,t;
    int *ar = malloc(n * sizeof(int));
    for (i = 0;i< n;i++)
    {
        ar[i]=area(tr[i].a,tr[i].b,tr[i].c);
    }
    for(i=0;i< n;i++)
    {
        for(j=0;j<n-i-1;j++)
        {
            if(ar[j]>ar[j+1])
            {
                t=ar[j];
                ar[j]=ar[j+1];
                ar[j+1]=t;
                temp=tr[j];
                tr[j]=tr[j+1];
                tr[j+1]=temp;
            }
        }
    }
}


int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}
