//https://www.hackerrank.com/challenges/restaurant/problem

/*Martha is interviewing at Subway. One of the rounds of the interview requires her to cut a bread of size l x b into smaller identical pieces such that each piece is a square having maximum possible side length with no left over piece of bread.

Input Format

The first line contains an integer T.T lines follow. Each line contains two space separated integers  and  which denote length and breadth of the bread.


Output Format

T lines, each containing an integer that denotes the number of squares of maximum size, when the bread is cut as per the given condition.

Sample Input 0

2
2 2
6 9
Sample Output 0

1
6
Explanation 0

The 1st testcase has a bread whose original dimensions are 2 x 2, the bread is uncut and is a square. Hence the answer is 1.
The 2nd testcase has a bread of size 6 x 9. We can cut it into 54 squares of size 1 x 1, 6 of size 3 x 3. For other sizes we will have leftovers. Hence, the number of squares of maximum size that can be cut is 6.
*/

/*Solution*/

#include <bits/stdc++.h>
using namespace std;

int main()
{
   int T;
    scanf("%d",&T);
    while(T--)
      {
      int L,B,i=2;
        scanf("%d %d",&L,&B);
        while(L!=1 && B!=1 && i<=B && i<=L)
        {
            if(L%i==0 && B%i==0)
            {
                L=L/i;
                B=B/i;
            }
            else
            i++;
        }
        printf("%d\n",L*B);
    }
    return 0;
}
