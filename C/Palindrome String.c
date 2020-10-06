// C Program for finding Palindrome String
#include<stdio.h>
#include<string.h>
main()
{
	char a[25],b[25];
	int c;
	printf("Enter a string:");
	gets(a);
	strcpy(b,a);//Copying input string
	strrev(a);//Reverse the input string
	c=strcmp(a,b);//Comparing the reverse string with the copy of the input string
	if(c==0)
	{
		printf("Entered string is a palindrome.");
	}
	else
	{
		printf("Entered string is not a palindrome.");
	}
}
