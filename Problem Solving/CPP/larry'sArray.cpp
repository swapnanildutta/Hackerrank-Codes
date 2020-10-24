// Larry has been given a permutation of a sequence of natural numbers incrementing from  as an array. He must determine whether the array can be sorted using the following operation any number of times:

// Choose any  consecutive indices and rotate their elements in such a way that ABC-->BCA-->CAB-->ABC.
// For example, if :A={1,6,5,2,4,3};

// A		rotate 
// [1,6,5,2,4,3]	[6,5,2]
// [1,5,2,6,4,3]	[5,2,6]
// [1,2,6,5,4,3]	[5,4,3]
// [1,2,6,3,5,4]	[6,3,5]
// [1,2,3,5,6,4]	[5,6,4]
// [1,2,3,4,5,6]

// YES

// On a new line for each test case, print YES if A can be fully sorted. Otherwise, print NO.
















#include <bits/stdc++.h>

using namespace std;
   
int main() {
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n;
        int arr[1000];
        cin>>n;
        for (int i=0;i<n;i++)cin>>arr[i];
        int inv = 0;
        for (int i=0;i<n;i++)
           
           { 
               for (int j=i+1;j<n;j++)
                if (arr[i] > arr[j])
                    inv ++;
           }
        if (inv%2==0)cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
            
    }
    return 0;

}
