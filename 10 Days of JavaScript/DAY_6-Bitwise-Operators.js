/*DAY-6*/
/*Objective

Today, we're practicing bitwise operations. Check the attached tutorial for more details.

Task

We define  to be a sequence of distinct sequential integers from  to ; in other words, . We want to know the maximum bitwise AND value of any two integers,  and  (where ), in sequence  that is also less than a given integer, .

Complete the function in the editor so that given  and , it returns the maximum .

Note: The  symbol represents the bitwise AND operator.

Input Format

The first line contains an integer, , denoting the number of function calls.
Each of the  subsequent lines defines a dataset for a function call in the form of two space-separated integers describing the respective values of  and .

Constraints

Output Format

Return the maximum possible value of  for any  in sequence .

Sample Input 0

3
5 2
8 5
2 2
Sample Output 0

1
4
0
Explanation 0

We perform the following  function calls:

When  and , we have the following possible  and  values in set :

The maximum of any  that is also  is , so we return .

When  and , the maximum of any  in set  is  (see table above), so we return .
When  and , the maximum of any  in set  is  (see table above), so we return .
Sample Input 1

2
9 2
8 3
Sample Output 1

1
2
Explanation 1

We perform the following  function calls:

When  and , the maximum of any  in set  is  (see table above), so we return .
When  and , the maximum of any  in set  is  (see table above), so we return .
*/

/*SOLUTION*/


function getMaxLessThanK(n, k){
    return (((k | (k - 1)) > n) ? (k -2) : (k - 1));
}
