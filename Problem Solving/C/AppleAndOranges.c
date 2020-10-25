// Question
// Apple and Orange

// Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, determine the number of apples and oranges that land on Sam's house.

// In the diagram below:

//     The red region denotes the house, where 

// is the start point, and
// is the endpoint. The apple tree is to the left of the house, and the orange tree is to its right.
// Assume the trees are located on a single point, where the apple tree is at point
// , and the orange tree is at point
// .
// When a fruit falls from its tree, it lands
// units of distance from its tree of origin along the -axis. *A negative value of means the fruit fell units to the tree's left, and a positive value of means it falls units to the tree's right. *

// Giveethe value of d for m apples and n oranges, determine how many apples and oranges will fall on Sam's house(i.e in the inclusive range[s,t])?
// For example, Sam's House is between s = 7 and t = 10. The apple tree is located at a = 4 and the orange at b = 12. There are m=3 apples and n=3 oranges. Apples are thrown apples=[2,3,-4] unit distance from a
// and oranges = [3,-2,-4] units distance. Adding each apples distance to the position of the tree, they land at [4+2,4+3,4+-4] = [6,7,0]. Oranges land at [12+3,12+-2,12+-4] = [15,10,8]. One apple and two oranges
// land in the inclusive range 7-10 so we print

// 	1
// 	2


// Function Description

// Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges that land on Sam's house, each on a separate line.

// countApplesAndOranges has the following parameter(s):

//     s: integer, starting point of Sam's house location.
//     t: integer, ending location of Sam's house location.
//     a: integer, location of the Apple tree.
//     b: integer, location of the Orange tree.
//     apples: integer array, distances at which each apple falls from the tree.
//     oranges: integer array, distances at which each orange falls from the tree.



// Input Format

// The first line contains two space-separated integers denoting the respective values of s
// and t.
// The second line contains two space-separated integers denoting the respective values of a and b.
// The third line contains two space-separated integers denoting the respective values of m and n.
// The fourth line contains m space-separated integers denoting the respective distances that each apple falls from point a.
// The fifth line contains n space-separated integers denoting the respective distances that each orange falls from point b.

// Constraints
// 	1 <=s,t,a,b,m,n <= 10^5
// 	-10^5 <= d <= 10^5
// 	a < s < t < b

// Sample Input 0

// 7 11
// 5 15
// 3 2
// -2 2 1
// 5 -6

// Sample Output 0

// 1
// 1





// Solution


#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
	int s,t,a,b,m,n,acount=0,ocount=0,i;
	int apple[100002],orange[100002];
	scanf("%d %d",&s,&t);
	scanf("%d %d",&a,&b);
	scanf("%d %d",&m,&n);
	for (i = 0; i < m; ++i)
	{
		scanf("%d",&apple[i]);
		apple[i] = apple[i] + a;
	}
	for (i = 0; i < n; ++i)
	{
		scanf("%d",&orange[i]);
		orange[i] = orange[i] + b;
	}
	for (i = 0; i < m ; i++)
	{
		if (apple[i] >= s && apple[i] <= t )
		{
			acount = acount + 1;
		}
	}
	for (i = 0; i < n; i++)
	{
		if (orange[i] >= s && orange[i] <= t )
		{
			ocount = ocount + 1;
		}
	}
	printf("%d\n",acount);
	printf("%d",ocount);
}