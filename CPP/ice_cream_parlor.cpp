


/*

Problem Statement:

Sunny and Johnny like to pool their money and go to the ice cream parlor. Johnny never buys the same flavor that Sunny does. The only other rule they have is that they spend all of their money.

Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

For example, they have m=6 to spend and there are flavors costing cost = [1,3,4,5,6]. The two flavors costing 1 and 5 meet the criteria. Using 1-based indexing, they are at indices 1 and 4.

Function Description

Complete the icecreamParlor function in the editor below. It should return an array containing the indices of the prices of the two flavors they buy, sorted ascending.

icecreamParlor has the following parameter(s):

m: an integer denoting the amount of money they have to spend
cost: an integer array denoting the cost of each flavor of ice cream

Input Format

The first line contains an integer,t, denoting the number of trips to the ice cream parlor. The next t sets of lines each describe a visit. Each trip is described as follows:

1. The integer m, the amount of money they have pooled.
2. The integer n, the number of flavors offered at the time.
3. space-separated integers denoting the cost of each flavor:
 	cost[cost[1],cost[2],.....,cost[n]].
Note: The index within the cost array represents the flavor of the ice cream purchased.

Constraints
1<=t<=50
2<=m<=10000
2<=n<=10000
1<=cost[i]<=10000, ∀ i belongs to [1,n] 
There will always be a unique solution.
Output Format

For each test case, print two space-separated integers denoting the indices of the two flavors purchased, in ascending order.

Sample Input

2
4
5
1 4 5 3 2
4
4
2 2 4 3
Sample Output

1 4
1 2
*/


#include<bits/stdc++.h>
using namespace std;
int main(){
int t;
cin>>t;
for(int i=0;i<t;i++){
    int n,m,a,b;
    cin>>m>>n;
    int arr[n];
    for(int j=1;j<=n;j++) cin>>arr[j];
    for(int j=1;j<n;j++){
        for(int k=j+1;k<=n;k++){
            if(arr[j]+arr[k]==m) {
                a=j;
                b=k;
                break;
            }
        }
    }
    if(a<=b) cout<<a<<" "<<b<<endl;
    else cout<<b<<" "<<a<<endl;
}

}

