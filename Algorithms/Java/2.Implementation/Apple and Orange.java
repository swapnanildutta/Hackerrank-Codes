// Complete the countApplesAndOranges function below.
static void countApplesAndOranges(int s, int t, int a, int b, int[] apples, int[] oranges) {
    int ac = 0;
    int oc = 0;
    for(int i = 0 ; i< apples.length ; i++ ){
        apples[i] += a;
        if(apples[i] >= s && apples[i] <= t){
            ac++;
        }
    }
    for(int i = 0 ; i< oranges.length ; i++ ){
        oranges[i] += b;
        if(oranges[i] >= s && oranges[i] <= t){
            oc++;
        }
    }
    System.out.println(ac);
    System.out.println(oc);
}

   