/*
LINK = https://www.hackerrank.com/challenges/maximum-draws/problem

A person is getting ready to leave and needs a pair of matching socks. If there are n colors of socks in the drawer, how many socks need to be removed to be certain of having a matching pair?

Example n = 2

There are 2 colors of socks in the drawer. If they remove 2 socks, they may not match. The minimum number to insure success is 3.

Function Description

Complete the maximumDraws function in the editor below.

maximumDraws has the following parameter:

int n: the number of colors of socks
Returns

int: the minimum number of socks to remove to guarantee a matching pair.
Input Format
The first line contains the number of test cases, t.
Each of the following t lines contains an integer n.


Sample Input

2
1
2
Sample Output

2
3
Explanation
Case 1 : Only 1 color of sock is in the drawer. Any 2 will match.
Case 2 : 2 colors of socks are in the drawer. The first two removed may not match. At least 3 socks need to be removed to guarantee success.
*/

#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the maximumDraws function below.
 */
int maximumDraws(int n) {
  
  /**
  the whole idea is to understand the worst case scenario..
  suppose its your bad day, and you are getting late for the office but you couldn't find a pair of socks (of same color)
  as you are having n number of different color socks
  you must pull out n socks to ensure that in next turn when to pull another sock EUREKA!! IT'S MATCH.
  **/

     return n+1;

}

//pre-written code [dont bother much]
int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int t_itr = 0; t_itr < t; t_itr++) {
        int n;
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        int result = maximumDraws(n);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}
