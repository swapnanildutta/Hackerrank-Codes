# counting number of triplets with a common difference between each element of the triplets



def countTriplets(d, arr):
    l=len(arr)
    m=0
    for i in range(l):
        a=arr[i]+d
        b=arr[i]+(2*d)
        c=0
        p=0
        for j in range(i+1,l):
            if arr[j]==a:
                c=j
                p=-1
                break
        if p==-1:
            for k in range(c+1,l):
                if arr[k]==b:
                    m+=1
                    break
    return m

    
n=int(input('Enter the size of array '))
d=int(input('Enter the common difference between element of triplet '))


arr=[int(input('Enter {0}th element of array '.format(i+1))) for i in range(n)]
no_of_triplet=countTriplets(d,arr)
print('Number of triplet with {0} common difference between terms is '.format(d),no_of_triplet)
