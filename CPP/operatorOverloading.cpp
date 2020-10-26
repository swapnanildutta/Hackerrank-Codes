/*Classes define new types in C++. Types in C++ not only interact by means of constructions and assignments but also via operators. For example:

int a=2, b=1, c;
c = b + a;
The result of variable c will be 3.
Similarly, classes can also perform operations using operator overloading. 
Operators are overloaded by means of operator functions, which are regular functions with special names. 
Their name begins with the operator keyword followed by the operator sign that is overloaded. The syntax is:

type operator sign (parameters) { /*... body ...*/ }
You are given a main() function which takes a set of inputs to create two matrices and prints the result of their addition. 
You need to write the class Matrix which has a member a of type vector<vector<int> >. 
You also need to write a member function to overload the operator +. The function's job will be to add two objects of Matrix type and return the resultant Matrix.
*/


#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
class Matrix
{
public:
vector<vector<int> > a;

Matrix & operator + (const Matrix &y)
{
for (int m=0; m<y.a.size(); ++m)
{
for (int n=0; n<y.a[0].size(); ++n)
{
this->a[m][n] = this->a[m][n] + y.a[m][n];
}
}
return *this;
}

};
int main () {
   int cases,k;
   cin >> cases;
   for(k=0;k<cases;k++) {
      Matrix x;
      Matrix y;
      Matrix result;
      int n,m,i,j;
      cin >> n >> m;
      for(i=0;i<n;i++) {
         vector<int> b;
         int num;
         for(j=0;j<m;j++) {
            cin >> num;
            b.push_back(num);
         }
         x.a.push_back(b);
      }
      for(i=0;i<n;i++) {
         vector<int> b;
         int num;
         for(j=0;j<m;j++) {
            cin >> num;
            b.push_back(num);
         }
         y.a.push_back(b);
      }
      result = x+y;
      for(i=0;i<n;i++) {
         for(j=0;j<m;j++) {
            cout << result.a[i][j] << " ";
         }
         cout << endl;
      }
   }  
   return 0;
}
