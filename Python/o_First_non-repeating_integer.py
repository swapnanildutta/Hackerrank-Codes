n = int(input())
for i in range(n):
    s = int(input())
    a = list(map(int,input().strip().split()))[:s]
    for i in range(len(a)): 
        j = 0
        while(j < len(a)): 
            if (i != j and a[i] == a[j]): 
                break
            j += 1
        if (j == len(a)): 
            print(a[i]) 
