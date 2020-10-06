//Author: Shrey Rai
//Problem: Max Min

/*
Problem Statement: You will be given a list of integers, arr , and a single integer k.
You must create an array of length k from elements of such that its unfairness is minimized.
Call that array . Unfairness of an array is
calculated as: max(subarr)-min(subarr)
Where:
- max denotes the largest integer in subarr
- min denotes the smallest integer in subarr
*/

/*
Function Description

Complete the maxMin function in the editor below. It must return an integer that denotes the minimum possible value of unfairness.

maxMin has the following parameter(s):

k: an integer, the number of elements in the array to create
arr: an array of integers
*/


/*
Constraints:
n<=100000
k<=n
arr[i]<=10^9
*/

/*
Sample Input 0

7
3
10
100
300
200
1000
20
30
Sample Output 0

20
////////////
Sample Input 1

10
4
1
2
3
4
10
20
30
40
100
200
Sample Output 1

3

//////////////
Sample Input 2

5
2
1
2
1
2
1
Sample Output 2

0
*/
#include <bits/stdc++.h>
using namespace std;
#define m 1000000007

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  long long int n, k, i, mini = 1000000000;
  cin >> n >> k;
  long long int arr[n];
  for (i = 0; i < n; i++)
    cin >> arr[i];
  sort(arr, arr + n);
  for (i = 0; i < n - k + 1; i++) {
    if (arr[i + k - 1] - arr[i] < mini)
      mini = arr[i + k - 1] - arr[i];
  }
  cout << mini;
  return 0;
}

