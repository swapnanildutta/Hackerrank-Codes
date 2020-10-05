/*

Question
Welcome to the last day! Today, we're discussing bitwise operations. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given set
. Find two integers, and (where ), from set such that the value of is the maximum possible and also less than a given integer, . In this case,

represents the bitwise AND operator.

Input Format

The first line contains an integer,
, the number of test cases.
Each of the subsequent lines defines a test case as space-separated integers, and

, respectively.

Constraints

Output Format

For each test case, print the maximum possible value of

on a new line.

Sample Input

3
5 2
8 5
2 2

Sample Output

1
4
0

Explanation

All possible values of and

are:

The maximum possible value of that is also is , so we print on a new line.

*/
fun main(args: Array<String>) {
    var T=readLine()!!.toInt();
    while(T-->0){
        val query=readInts().toTypedArray();
       println(findMax(query[0], query[1]));
    }
    
}
private fun findMax(n:Int,k:Int):Int{
    var max=0;
    var a=n-1;
    while(a-->0){
        for(b in (a+1)..n){
            val temp=a and b;
            if(temp<k && temp>max){
                max=temp;
            }
        }
    }
    return max;

}
private fun readLn() = readLine()!! ;
private fun readInt() = readLn().toInt();
private fun readStrings() = readLn().split(" ") ;
private fun readInts() = readStrings().map { it.toInt() } 