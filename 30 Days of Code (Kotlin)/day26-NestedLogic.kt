/*
Question
Today's challenge puts your understanding of nested conditional statements to the test. You already have the knowledge to complete this challenge, but check out the Tutorial tab for a video on testing!

Task
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

    If the book is returned on or before the expected return date, no fine will be charged (i.e.: 

.
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date,
.
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the
.
If the book is returned after the calendar year in which it was expected, there is a fixed fine of

    .

Input Format

The first line contains
space-separated integers denoting the respective , , and on which the book was actually returned.
The second line contains space-separated integers denoting the respective , , and

on which the book was expected to be returned (due date).

Constraints

Output Format

Print a single integer denoting the library fine for the book received as input.

Sample Input

9 6 2015
6 6 2015

Sample Output

45

Explanation

Given the following return dates:
Actual:

Expected: Because , we know it is less than a year late.
Because , we know it's less than a month late.
Because

, we know that it was returned late (but still within the same month and year).

Per the library's fee structure, we know that our fine will be
. We then print the result of as our output.
 */


fun main(args: Array<String>) {
    var actualDate=readInts().toTypedArray();
    var expectedDate=readInts().toTypedArray();

    var fine=0;
    if(expectedDate[2]==actualDate[2]){
        if(expectedDate[1]<actualDate[1]){
            fine=(actualDate[1]-expectedDate[1])*500;
        }else if((expectedDate[1]==actualDate[1])&&(expectedDate[0]<actualDate[0])){
            fine=(actualDate[0]-expectedDate[0])*15;
        }
    }else if(expectedDate[2]<actualDate[2]){
        fine=10000;
    }
    println(fine);
}
private fun readLn() = readLine()!! ;
private fun readInt() = readLn().toInt();
private fun readStrings() = readLn().split(" ") ;
private fun readInts() = readStrings().map { it.toInt() } 