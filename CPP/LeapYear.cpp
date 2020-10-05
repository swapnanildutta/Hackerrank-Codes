#include<iostream.h>
#include<conio.h>

void main()
{
	clrscr();
	int yr, result  = 0;
	cout<<"\nEnter a year to test";
	cin>>yr;

	result = is_leap(yr);

	if(result == 1)
	 cout<<yr<<"\n is a leap year.";

	else
	 cout<<yr<<"\n is not a leap year.";

	getch();
}

int is_leap(year)
{
	if(((year%4==0 && year%100!=0) || year%400==0) && year>=1900)
	return(1);

	else
	return(0);
}