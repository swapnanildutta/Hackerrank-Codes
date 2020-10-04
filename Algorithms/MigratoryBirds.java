//solution of Migratory Birds 
//Practice => Algorithms => Implementation => Migratory Birds

import java.util.*;
class MigratoryBirds 
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int arr[]=new int[n];
        for(int i=0;i<arr.length;i++)
        {
            arr[i]=sc.nextInt();
        }
        Arrays.sort(arr);
        HashMap<Integer,Integer> hm=new HashMap<Integer,Integer>();
        for(int i=0;i<arr.length;i++)
        {
            if(hm.containsKey(arr[i]))
            {
                hm.put(arr[i],hm.get(arr[i])+1);
            }
            else
            {
                hm.put(arr[i],1);
            }
        }
        int x=0;
        int y=-1;
        for(Map.Entry<Integer,Integer> set:hm.entrySet())
        {
            if(x<set.getValue())
            {
                x=set.getValue();
                y=set.getKey();
            }
            
        }
        System.out.println(y);
    }
}
