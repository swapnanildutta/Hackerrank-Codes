# BINARY SEARCH ALGORITHM
#implementation done using the recursive method

# Returns index of x in arr if present, else -1 
def BinarySearch(array, low, high, x): 
 
    if low <= high: 
        middle = (high + low)//2
        #middle case 
        if array[mid] == x: 
            return mid 
        #smaller than middle case  
        elif array[mid] > x: 
            return binary_search(array, low, middle-1, x) 
        #right side case 
        else: 
            return binary_search(array, middle+1, high, x) 
    else: 
        #not found case
        return -1
  
#example for array
array = [1, 7, 12, 14, 23, 79, 123]

#get input to search for as an integer number
x = int(input("enter a number: "))
  
res = BinarySearch(array, 0, len(array)-1, x) 

#condition of existance
if res != -1: 
    print("number found at position: " + str(result)) 
else: 
    print("number not found ! :(") 
