public class Solution {

    // Complete the arrayManipulation function below.
    static long arrayManipulation(int n, int[][] queries) {
    long[] ret=new long[n];
        int i;
        int j;
    for(i=0;i<n;i=i+1)
        ret[i]=0;
    for( i=0;i<queries.length;i=i+1)
    {
        ret[queries[i][0]-1]+=queries[i][2];
        if(queries[i][1]<n)
        ret[queries[i][1]]-=queries[i][2];
    }
    long max=0;
    long x=0;
    for( i=0;i<n;i=i+1)
    {
        x+=ret[i];
        //printf("%lld ",x);
        if(x>max)
        max=x;
    }
    return max;
    }
