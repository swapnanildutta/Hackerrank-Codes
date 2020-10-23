#include <bits/stdc++.h>
using namespace std;

int findMax(deque<int> d)
{
    int Max=INT_MIN;
    for(int i=0; i<d.size() ;++i) 
    {
        if(d[i]>Max)
            Max=d[i];
    }
    
    return Max;
}

int main(){
    int t;
    cin >>t;
    while(t--) 
    {
        int n,k;
        cin>>n>>k;
        int arr[n];
        for(int i=0; i<n ;++i)
        {
            cin>>arr[i];
        }

        int mx;
        deque<int> dq;
        for(int i=0; i<k ;++i) 
        {
            dq.push_back(arr[i]);
        }
        
        mx=findMax(dq);
        cout<<mx<<" ";
        
        for(int i=k; i<n ;++i) 
        {
            int pop=dq.front();
            dq.pop_front();
            dq.push_back(arr[i]);

            if(mx==pop) 
            {
                mx=findMax(dq);
            }
            else if(arr[i]>mx) 
            {
                mx=arr[i];
            }
            
            cout<<mx<<" ";
        }
        cout<<endl;
    }
     
     return 0;
}
