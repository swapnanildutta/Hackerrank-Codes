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
