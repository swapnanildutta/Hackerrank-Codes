/* 
Question
In this challenge, you'll work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!

Input Format

There are
lines of numeric input:
The first line has a double, (the cost of the meal before tax and tip).
The second line has an integer, (the percentage of being added as tip).
The third line has an integer, (the percentage of

being added as tax).

Output Format

Print the total meal cost, where
is the rounded integer result of the entire bill (

with added tax and tip).

Sample Input

12.00
20
8

Sample Output

15

Explanation

Given:
, , Calculations:



We round to the nearest dollar (integer) and then print our result, .
*/
import java.io.*
import java.math.*
import java.security.*
import java.text.*
import java.util.*
import java.util.concurrent.*
import java.util.function.*
import java.util.regex.*
import java.util.stream.*
import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.io.*
import kotlin.jvm.*
import kotlin.jvm.functions.*
import kotlin.jvm.internal.*
import kotlin.ranges.*
import kotlin.sequences.*
import kotlin.text.*

// Complete the solve function below.
fun solve(meal_cost: Double, tip_percent: Int, tax_percent: Int): Unit {

    val tip:Double = meal_cost*(tip_percent.toDouble()/100);
    val tax:Double = meal_cost*(tax_percent.toDouble()/100);
    val totalCost:Double = meal_cost + tip + tax;

    print(Math.round(totalCost));
}

fun main() {
    val scan = Scanner(System.`in`)

    val meal_cost = scan.nextLine().trim().toDouble()

    val tip_percent = scan.nextLine().trim().toInt()

    val tax_percent = scan.nextLine().trim().toInt()

    solve(meal_cost, tip_percent, tax_percent)
}
