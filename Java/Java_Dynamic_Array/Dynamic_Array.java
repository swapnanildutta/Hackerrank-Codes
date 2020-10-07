/*
Create a list, seqList, of n empty sequences, where each sequence is indexed from 0 to n-1. The elements within each of the n sequences also use 0-indexing.
Create an integer, lastAnswer, and initialize it to 0.
There are 2 types of queries that can be performed on the list of sequences:
Query: 1 x y
Find the sequence, seq, at index ((x xor lastAnswer) % n) in seqList.
Append integer y to sequence seq.
Query: 2 x y
Find the sequence, seq, at index ((x xor lastAnswer) % n) in seqList.
Find the value of element y % size in  seq(where size is the size of seq) and assign it to lastAnswer.
Print the new value of lastAnswer on a new line.
Note:  is the bitwise XOR operation, which corresponds to the ^ operator in most languages. Learn more about it on Wikipedia.  is the modulo operator.

Function Description

Complete the dynamicArray function below.

dynamicArray has the following parameters:
- int n: the number of empty sequences to initialize in seqList
- string queries[q]: an array of query strings

Returns

int[]: the results of each type 2 query in the order they are presented
Input Format

The first line contains two space-separated integers,  n(the number of sequences) and  q(the number of queries), respectively.
Each of the q subsequent lines contains a query in the format defined above, queries[i].

Constraints
1 <= n,q <= 10^5
0 <= x <= 10^9
0 <= y <= 10^9

It is guaranteed that query type 2 will never query an empty sequence or index.
Sample Input

2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1
Sample Output

7
3
*/
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'dynamicArray' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. 2D_INTEGER_ARRAY queries
     */

    public static List<Integer> dynamicArray(int n, List<List<Integer>> queries) {
    
        List<Integer>[] ans = new ArrayList[n];
        List <Integer> r = new ArrayList<Integer>();
        int lastAnswer = 0;

        for(int i=0;i<n;i++)
        {
            ans[i] = new ArrayList<>();
        }
        for(int i=0;i<queries.size();i++)
        {
            int x = queries.get(i).get(1);
            int y = queries.get(i).get(2);
            int seq = (x^lastAnswer)%n;
            List<Integer> ans1 = ans[seq];
            if(queries.get(i).get(0)==1)
            {
                ans1.add(y);
            }
            else
            {
                lastAnswer = ans1.get((y%ans1.size()));
                r.add(lastAnswer);
            }
        }
        return r;
    }

}

public class Dynamic_Array {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int q = Integer.parseInt(firstMultipleInput[1]);

        List<List<Integer>> queries = new ArrayList<>();

        IntStream.range(0, q).forEach(i -> {
            try {
                queries.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        List<Integer> result = Result.dynamicArray(n, queries);

        bufferedWriter.write(
            result.stream()
                .map(Object::toString)
                .collect(joining("\n"))
            + "\n"
        );

        bufferedReader.close();
        bufferedWriter.close();
    }
}