#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int t,i,j,n;
    cin>>t;
    while(t-->0)
    {
        cin>>n;
        if(n<=1)
        {
            cout<<"Not prime\n";
            continue;
        }
        else if(n<=3)
        {
            cout<<"Prime\n";
            continue;
        }
        int num=pow(n,0.5);
        //cout<<num<<endl;
        for(i=2;i<=num;i++)
        {
            if(n%i==0)
            {
                cout<<"Not prime\n";
                break;
            }
        }
        if(i==num+1)
            cout<<"Prime\n";
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
