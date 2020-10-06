/*
Hackerrank problem : https://www.hackerrank.com/challenges/handshake/problem
At the annual meeting of Board of Directors of Acme Inc. If everyone attending shakes hands exactly one time with every other attendee, how many handshakes are there?

Example
n = 3
There are attendees, p1, p2 and p3. p1 shakes hands with p2 and p3, and p2 shakes hands with p3. Now they have all shaken hands after 3 handshakes. 
*/
import java.io.PrintWriter

object Solution {

    /*
     * Complete the handshake function below.
     */
    def handshake(n: Int): Int = {
        /*
         * Write your code here.
         */
         n*(n-1)/2

    }

    def main(args: Array[String]) {
        val stdin = scala.io.StdIn

        val printWriter = new PrintWriter(sys.env("OUTPUT_PATH"))

        val t = stdin.readLine.trim.toInt

        for (tItr <- 1 to t) {
            val n = stdin.readLine.trim.toInt

            val result = handshake(n)

            printWriter.println(result)
        }

        printWriter.close()
    }
}
