static int getTotalX(int[] a, int[] b) {
    boolean var,var2;
    int i;
    int j;
    int m=0;
    for(i= a[a.length-1] ; i<=b[0] ; i++){
        var = false;
        for(j=0;j<a.length;j++){
            if(i%a[j]==0){
                var =true;
            }else{
                var =false;
                break;
            }
        }
        if(var==true){
            var2=false;
            for(int k=0;k<b.length;k++){
                if(b[k]%i==0){
                    var2=true;
                }else{
                    var2=false;
                    break;
                }
            }
             if(var2==true){
                    m++;
                }
        }
    }
   return m;
}