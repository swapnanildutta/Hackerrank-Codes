'''
Task
Create a list of numbers from 1 to 100 named list_1. The numbers should be present in the increasing order: Ex list_1 = [1,2,3,4,5,....,100]
Given an input let's say a, you have to print the number of elements of list_1 which are divisible by a,  excluding the element which is equal to a.

Input:
Number a
Output:
In a single line, the number of elements (i.e. the count and not the elements) which are divisible by a.

Example:
Input:
50
Output:
1
Explanation
Since there is only one number, i.e. 100 which is divisible by 50 and is in the list_1. We have to exclude the element 50 of list_1 because it is equal to the input.
'''

list_1=[]
for i in range(1,101):
    list_1.append(i)
a=int(input())
num=0
for item in list_1:
    if(item!=a):
        if(item%a==0):
            num=num+1
print(num)