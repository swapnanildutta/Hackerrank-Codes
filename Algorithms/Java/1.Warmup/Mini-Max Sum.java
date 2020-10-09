// Complete the miniMaxSum function below.
static void miniMaxSum(int[] arr) {
    long sum = 0;
    for(int i = 0; i< arr.length ; i++){
        sum += arr[i]; 
    }
    Arrays.sort(arr);
    long min = sum - arr[4];
    long max = sum - arr[0];
    System.out.print(min +" "+ max);
}

    