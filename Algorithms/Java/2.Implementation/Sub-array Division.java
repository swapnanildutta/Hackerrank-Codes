// Brute Force Solution
static int birthday(List<Integer> s, int d, int m) {
    int count = 0;
    for(int i = 0 ; i < s.size() ; i++){
        int sum = 0;
        int index = 0;
        for(int j = 0 ; j < m ; j++){
            if(j+i == s.size()) break;
            sum = sum + s.get(j+i);
        }
        if (sum == d){
            count++;
        }
    }
    return count;
}
//Sliding Window Technique
static int birthday(List<Integer> s, int d, int m) {
    int sum = 0 ; 
    int ways = 0;
    if(m <= s.size()){
        for(int i = 0 ; i < m ; i++){
            sum += s.get(i);
        }
        if(sum == d) 
            ways++;
    }
    for(int i = 0; i < s.size() - m; i++)
    {
        sum = sum - s.get(i) + s.get(i + m);
        if(sum == d) ways++;
    }
    return ways;
}

    