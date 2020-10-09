// Complete the compareTriplets function below.
static List<Integer> compareTriplets(List<Integer> a, List<Integer> b) {
    int ac = 0;
    int bc = 0;
    
    List<Integer> ans = new ArrayList<Integer>();
    for(int i = 0 ; i < a.size() ; i++){
        if (a.get(i) > b.get(i))
            ++ac;
        else if (a.get(i) < b.get(i))
            ++bc;
    }
    ans.add(ac);
    ans.add(bc);
    return ans;
}

    