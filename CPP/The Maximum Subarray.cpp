/*
 We define subsequence as any subset of an array. We define a subarray as a contiguous subsequence in an array.

Given an array, find the maximum possible sum among:

all nonempty subarrays.
all nonempty subsequences.
Print the two values as space-separated integers on one line.

Note that empty subarrays/subsequences should not be considered.

For example, given an array , the maximum subarray sum is comprised of element inidices  and the sum is . The maximum subsequence sum is comprised of element indices  and the sum is .

Function Description

Complete the maxSubarray function in the editor below. It should return an array of two integers: the maximum subarray sum and the maximum subsequence sum of .

maxSubarray has the following parameter(s):

arr: an array of integers
Input Format

The first line of input contains a single integer , the number of test cases.

The first line of each test case contains a single integer .
The second line contains  space-separated integers  where .

Constraints

The subarray and subsequences you consider should have at least one element.

Output Format

Print two space-separated integers denoting the maximum sums of nonempty subarrays and nonempty subsequences, respectively.

Sample Input 0

2
4
1 2 3 4
6
2 -1 2 3 4 -5
Sample Output 0

10 10
10 11
Explanation 0

In the first case: The maximum sum for both types of subsequences is just the sum of all the elements since they are all positive.

In the second case: The subarray  is the subarray with the maximum sum, and  is the subsequence with the maximum sum.

Sample Input 1

1
5
-2 -3 -1 -4 -6
Sample Output 1

-1 -1
Explanation 1

Since all of the numbers are negative, both the maximum subarray and maximum subsequence sums are made up of one element, .

*/

/*
SOLUTION EXPLANATION :-
 
 SUBARRAY SUM = this can be calculated with the help of kadanes algorithm .
 
 SUBSEQUENCE SUM = in any array of +ve and -ve elements  maximum sum will be sum of +ve integers.
 
 THERE IS 1 BASE CASE THAT IF THE WHOLE ARRAY IS -ve int that case both SUBSEQUENCE SUM and SUBARRAY SUM will be same and equal to max element of array.
 
 COMPLEXITY IS O(N LOG(N)) due to sorting .
 
 */
 #include <bits/stdc++.h>

using namespace std;


#include <bits/stdc++.h>

using namespace std;


int main(){
    int t,n;
    cin>>t;
    while(t--){
        cin>>n;
        int arr[n];
        int c=0;
        int cn=0,cs=0,p=0;
        for(int i=0;i<n;i++){  //SUBSEQUENCE SUM
            cin>>arr[i];
            if(arr[i]>0)
            p+=arr[i];
            else c++;
        }
        if(p==0){             //BASE CASE
            sort(arr,arr+n);
            p=arr[n-1];
        }
        for(int i=0;i<n;i++){   //SUBARRAY SUM
            cn+=arr[i];
            if(cn<0)cn=0;
            if(cn>cs){
                cs=cn;
            }
        }
        if(c==n){              //BASE CASE
            
            cs=p;
        }
        cout<<cs<<" "<<p<<endl;
    }
}
