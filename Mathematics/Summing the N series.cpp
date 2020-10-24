/*
    LINK = https://www.hackerrank.com/challenges/summing-the-n-series/problem

  
  Complete the summingSeries function below... its main idea is to obeserve the pattern of given series sum for T(1), T(2), T(3)..upto T(5)

  you will see one pattern for these results respectively...... 1, 4, 9, 16, 25

  to put it more concise way its nothing but a sum of odd numbers series i.e.  T(n) = n^2

  as a constraints are for large integers thus binary exponentiation seems ideal to use it here for more info on BINARY EXPONENTIATION
  you can go to one of very famous site among competitive programmers..worth checking out
  LINK = LINK - https://cp-algorithms.com/algebra/binary-exp.html


 */

#include <bits/stdc++.h>
typedef long long int lld;
using namespace std;
#define M 1000000007


int summingSeries(long n) {
    /*
     * your written code ahead.
     */
    lld b = 2;
    lld res = 1;

    n %= M;

    while(b > 0){

        if(b & 1)
            res = res%M * n%M;

        n = n%M * n%M;

        b >>= 1;
    }
    return res;
}


//already given boiler plate code ahead [no need to scratch your head]
int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int t_itr = 0; t_itr < t; t_itr++) {
        long n;
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        int result = summingSeries(n);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}
