 //Below is a program to find the largest array element in a given array using recursion.
// #define is used to initialize a value which is more like a constant.

// Problem Description
// This program will implement a one-dimentional array defining elements in unsorted fashion,
// in which we need to find largest element using Recursion method. 
//  The array used here is of type integer.

// To find the largest element,

// the first two elements of array are checked and the largest of these two elements are placed in arr[i]
// the first and third elements are checked and largest of these two elements is placed in arr[i].
// this process continues until the first and last elements are checked
// the largest number will be stored in the arr[i] position
// We have used a for loop to accomplish this task.

#include<stdio.h>
#include<conio.h>

#define MAX 100

int getMaxElement(int []);  // takes array of int as parameter
int size;

int main()
{
    int arr[MAX], max, i;
    printf("\n\nEnter the size of the array: ");
    scanf("%d", &size);
    printf("\n\nEnter %d elements\n\n", size);

    for(i = 0; i < size; i++)
    {
        scanf("%d", &arr[i]);
    }
    
    max = getMaxElement(arr);   // passing the complete array as parameter
    printf("\n\nLargest element of the array is %d\n\n", max);
    printf("\n\n\t\t\tCoding is Fun !\n\n\n");
    return 0;
}

int getMaxElement(int a[])
{
    static int i = 0, max =- 9999;  // static int max=a[0] is invalid
    if(i < size)   // till the last element
    {
        if(max < a[i])
        max = a[i];

        i++;    // to check the next element in the next iteration
        getMaxElement(a);   // recursive call
    }
    return max;
}
