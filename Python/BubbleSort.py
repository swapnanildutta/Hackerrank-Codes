#Python program for implementation og Bubble Sort
#Making Function to perform bubbleSort
def bubbleSort(arrays):
    for passnum in range(len(arrays)-1,0,-1):
        for i in range(passnum):
            if arrays[i]>arrays[i+1]:
                temp = arrays[i]
                arrays[i] = arrays[i+1]
                arrays[i+1] = temp
#initialize the array
arrays = [5,2,9,1,7,3,4,505,200]
#Performing bubbleSort Function
bubbleSort(arrays)
#Printing array after bubble sort
print(arrays)
