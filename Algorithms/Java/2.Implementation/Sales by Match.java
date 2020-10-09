import java.util.*;

public class Solution {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner (System.in);
        int n = sc.nextInt();
        HashMap<Integer,Integer> socks = new HashMap();

        for(int i = 0 ; i < n ; i++){
            int id = sc.nextInt();
            socks.put(id,socks.getOrDefault(id,0) + 1);
        }
        int count  = 0;
        for (Map.Entry<Integer, Integer> entry : socks.entrySet()) {
            int no = entry.getValue();
            while(no > 1){
                no-=2;
                count++;
            }
        }
        System.out.println(count);
    }
}
