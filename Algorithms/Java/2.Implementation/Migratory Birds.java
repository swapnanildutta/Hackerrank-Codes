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

public class Solution {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner (System.in);
        int n = sc.nextInt();
        HashMap<Integer,Integer> birds = new HashMap();

        for(int i = 0 ; i < n ; i++){
            int id = sc.nextInt();
            birds.put(id,birds.getOrDefault(id,0) + 1);
        }

        int maxcount = Collections.max(birds.values());
        for (Map.Entry<Integer, Integer> entry : birds.entrySet()) {
            if (entry.getValue().equals(maxcount)) {
                System.out.println(entry.getKey());
                break;
            }
        }
    }
}
