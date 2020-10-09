import java.io.*;
import java.math.*;
static int[] breakingRecords(int[] scores) {
    int maxscore = scores[0];
    int minscore = scores[0];
    int maxcount = 0;
    int mincount = 0;

    for(int i = 1 ; i< scores.length ; i++) {
        if(maxscore < scores[i]){
            maxscore = scores[i];
            maxcount++;
        }
        else if(minscore > scores[i]){
            minscore = scores[i];
            mincount++;
        }
    }
    int ans[] = new int[2];
    ans[0] = maxcount;
    ans[1] = mincount;
    return ans;
}