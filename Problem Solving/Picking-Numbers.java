/*
Picking Numbers:
Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to .

Example
a = [1,1,2,2,4,4,5,5,5]

There are two subarrays meeting the criterion: [1,1,2,2] and [4,4,5,5,5]. The maximum length subarray has 5 elements.

Function Description

Complete the pickingNumbers function in the editor below.

pickingNumbers has the following parameter(s):

int a[n]: an array of integers
Returns

int: the length of the longest subarray that meets the criterion
Input Format

The first line contains a single integer n, the size of the array a.
The second line contains n space-separated integers, each an a[i].

Constraints
2 <= n <= 100
0 < a[i] <=100

The answer will be >= 2.
Sample Input 0

6
4 6 5 3 3 1
Sample Output 0

3
Explanation 0

We choose the following multiset of integers from the array: {4,3,3}. Each pair in the multiset has an absolute difference <= 1 (i.e.|4-3| = 1,  and |3-3| = 0), so we print the number of chosen integers, 3 , as our answer.

Sample Input 1

6
1 2 2 3 1 2
Sample Output 1

5
Explanation 1

We choose the following multiset of integers from the array: {1,2,2,1,2}. Each pair in the multiset has an absolute difference <= 1 (i.e.,|1-2| = 1 ,|1-1| = 0 , and |2-2|= 0), so we print the number of chosen integers, 5, as our answer.*/




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
     * Complete the 'pickingNumbers' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts INTEGER_ARRAY a as parameter.
     */

    public static int pickingNumbers(List<Integer> a) {
    // Write your code here
    List<Integer> distinctNo=getDistinctNumbers(a);
        List<Integer> numbersLength=new ArrayList();
    
        
        int count=0;
        for (Iterator iterator = distinctNo.iterator(); iterator.hasNext();) {
            Integer integer = (Integer) iterator.next();
                //System.out.println(integer+" "+(integer+1));
                for (int i = 0; i < a.size(); i++) {
                    if(a.get(i)==integer || a.get(i)==integer+1)
                        count++;
                }
                //System.out.println("count "+count);
                numbersLength.add(count);
                count=0;
          
        }
        int max=numbersLength.get(0);
        for(int i=1;i<numbersLength.size();i++){
            if(numbersLength.get(i)>max)
                max=numbersLength.get(i);
        }
        return max;
    }
    private static List<Integer> getDistinctNumbers(List<Integer> a) {
        // TODO Auto-generated method stub
        List<Integer> d=new ArrayList<Integer>();
        
        for (Iterator iterator = a.iterator(); iterator.hasNext();) {
            Integer integer = (Integer) iterator.next();
            if(!d.contains(integer)){
                d.add(integer);
                //System.out.println(integer);
            }
        }
        
        return d;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> a = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        int result = Result.pickingNumbers(a);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
