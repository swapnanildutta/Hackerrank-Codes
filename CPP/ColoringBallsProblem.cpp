/* QUESTION */
/* Boboniu gives you

r red balls,
g green balls,
b blue balls,
w white balls.
He allows you to do the following operation as many times as you want:

Pick a red ball, a green ball, and a blue ball and then change their color to white.
You should answer if it's possible to arrange all the balls into a palindrome after 
several (possibly zero) number of described operations.

Input
The first line contains one integer T (1≤T≤100) denoting the number of test cases.

For each of the next T cases, the first line contains four integers r, g, b and w (0≤r,g,b,w≤109).

Output
For each test case, print "Yes" if it's possible to arrange all the balls into a palindrome after doing s
everal (possibly zero) number of described operations. Otherwise, print "No".*/

/* ANSWER */

#include<bits/stdc++.h>
#define MOD 998244353
#define IO ios_base::sync_with_stdio(false);cin.tie(NULL);
#define fo(i,a,b) for(i=a;i<b;i++)
#define mp make_pair
#define pb(x) push_back(x)
#define fi first
#define se second
typedef  long long  int ll;
typedef std::vector<ll> vi;
typedef std::vector<std::vector<ll> > vv;
#define print(vec,a,b) for(ll i=a;i<b;i++) cout<<vec[i]<<" ";cout<<endl;
#define all(a) a.begin(),a.end()
#define input(vec,a,b) for(ll i = a;i<b;i++) cin>>vec[i];
using namespace std;
const int N = 1e6+5;
void solve(){
            ll n,g,r,b,w;
            cin>>g>>r>>b>>w;
            ll ev=0,odd=0,e=0,o=0,zero = 0;
            //ev= odd=o=e =0;
            if(!g||!b||!r)
                zero = 1;
            if(g%2)
                ev++;
            else
                odd++;
            if(r%2)
                ev++;
            else
                odd++;
            if(b%2)
                ev++;
            else
                odd++;
            if(w%2)
                e++;
            else
                o++;
            //cout<<ev<<" "<<odd<<endl;
            if((odd==3)||(ev==3))
            {
                cout<<"YES"<<endl;return ;
            }
            if((ev==2)&&(!zero)&&e==1)
            {
                cout<<"YES"<<endl;return ;
            }
            if(ev==1&&o==1)
            {
                cout<<"YES"<<endl;return ;
            }
            cout<<"NO"<<endl;
}

 
int main()
{
      IO;
      ll t=1,i;
      cin>>t;
 
 
      while(t--)
      {
 
          solve();
      }
    return 0;
}