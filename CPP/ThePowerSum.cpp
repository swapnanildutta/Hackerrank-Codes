//Have A good Day Visitor
//Author: Saksham Goel

//Link To the problem : https://www.hackerrank.com/challenges/the-power-sum/problem

/*
Problem Description:

Find the number of ways that a given integer, X , can be expressed as the Nth sum of the  powers of unique, natural numbers.
For example, if X = 13 and N=2 , we have to find all combinations of unique squares adding up to 13. 
The only solution is 2^2+3^2.

Function Description

Complete the powerSum function in the editor below. It should return an integer that represents the number of possible combinations.

powerSum has the following parameter(s):
	X: the integer to sum to
	N: the integer power to raise numbers to

Input Format

The first line contains an integer X.
The second line contains an integer N.

Constraints

	1<=X<=1000
	2<=N<=10

Output Format

	Output a single integer, the number of possible combinations caclulated.

Sample Input 0

	10
	2
Sample Output 0

	1

*/

#include<bits/stdc++.h>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<math.h>
#include<sstream>
#include<string.h>
using namespace std;
#define endl "\n"
#define lli long long int
int value=0;
int check(int num,int n,int power){
    int val=num-pow(n,power);
    if(val<0) 
    return 0;
    else if(val==0)
    return 1;
    else 
    {
        return check(val,n+1,power)+check(num,n+1,power);
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int n,_pow;
    cin>>n>>_pow;
    cout<<check(n,1,_pow);
    return 0;
}

