/*
Question
Today, we're building on our knowledge of Arrays by adding another dimension. Check out the Tutorial tab for learning materials and an instructional video!

Context
Given a
2D Array,

:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in
to be a subset of values with indices falling in this pattern in

's graphical representation:

a b c
  d
e f g

There are
hourglasses in

, and an hourglass sum is the sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in

, then print the maximum hourglass sum.

Input Format

There are
lines of input, where each line contains space-separated integers describing 2D Array ; every value in will be in the inclusive range of to

.

Constraints

Output Format

Print the largest (maximum) hourglass sum found in

.

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output

19

Explanation

contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0

The hourglass with the maximum sum (

) is:

2 4 4
  2
1 2 4
 */

import java.util.Scanner
fun main(args: Array<String>) {
    var matrix=Array(6){IntArray(6)}

    val input = Scanner(System.`in`);
    
    for(i in 0..5){
        for(j in 0..5){
            matrix[i][j]=input.nextInt();
        }
    }

   var sum=Int.MIN_VALUE;
   
   for(i in 0..3){
       for(j in 0..3){
           val curSum=matrix[i][j] + matrix[i][j+1] + matrix[i][j+2]+ matrix[i+1][j+1]+ matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2];
           if(curSum>sum){
               sum=curSum;
           }
       }
   }

   print(sum);
}
