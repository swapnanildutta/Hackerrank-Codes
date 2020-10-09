static void bonAppetit(List<Integer> bill, int k, int b) {
    int sum = bill.stream().mapToInt(i -> i).sum();
    int t = b - (sum - bill.get(k))/2;
    System.out.println(t == 0 ? "Bon Appetit" : t);       
}

