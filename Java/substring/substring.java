public class Substring{  
  public static void main(String args[]){  
   String[] s = {"SachinTendulkar",null,"sdplkar","dyeljrqasderr"};
   
   for(int i = 0; i < s.length; i ++) {
     //handle string for null
     if(s[i] != null && s[i].length() > 10){ 
      System.out.println(s[i].substring(0,6));
     }
   }
  }
}
