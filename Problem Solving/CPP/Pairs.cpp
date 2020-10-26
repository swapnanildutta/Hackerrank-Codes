/*
Pairs
You will be given an array of integers and a target value. Determine the number of pairs of array elements
that have a difference equal to a target value.
For example, given an array of [1, 2, 3, 4] and a target value of 1, we have three values meeting the
condition: , , and .
Function Description
Complete the pairs function below. It must return an integer representing the number of element pairs
having the required difference.
pairs has the following parameter(s):
k: an integer, the target difference
arr: an array of integers
Input Format
The first line contains two space-separated integers and , the size of and the target value.
The second line contains space-separated integers of the array arr.
Constraints
each integer will be unique
Output Format
An integer representing the number of pairs of integers whose difference is .
Sample Input
5 2
1 5 3 4 2
Sample Output
3
Explanation
There are 3 pairs of integers in the set with a difference of 2: [5,3], [4,2] and [3,1] .
*/

#include<bits/stdc++.h>
using namespace std;
#define ll unsigned long long int
#define mp make_pair
#define pb push_back
typedef vector<ll> vll;
typedef pair<ll,ll> pll;
typedef vector<pll> vpll;
typedef map<pll,ll> mpll;
typedef map<ll,ll> mll;
int main()
{
    ll n,k;
    cin>>n>>k;
    vll a(n);
    mll hash;
    mpll pairHash;
    vpll result;
    for(auto &i:a)cin>>i,hash[i]=1;
    for(auto &i:a){
        if(hash.find(k+i)!=hash.end()){
            result.pb(mp(k+i,i));
        }
    }
    cout<<result.size();
}
