/*
 * Complete the 'birthdayCakeCandles' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY candles as parameter.
 */
public static int birthdayCakeCandles(List<Integer> candles) {
// Write your code here
    Collections.sort(candles);
    int max = candles.get(candles.size()-1);
    int c = 0;
    for(int i = 0 ; i < candles.size() ; i++ ){
        if(candles.get(i) == max){
            c++;
        }
    }
    return c;
}


