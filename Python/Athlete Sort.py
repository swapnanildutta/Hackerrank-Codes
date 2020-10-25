'''You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the Kth attribute and print the final resulting table. Follow the example given below for better understanding.

image

Note that K is indexed from 0 to M-1, where M is the number of attributes.

Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

Input Format

The first line contains N and M separated by a space.
The next  lines each contain M elements.
The last line contains K.

Output Format

Print the  lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

Sample Input 0

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
Sample Output 0

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
Explanation 0

The details are sorted based on the second attribute, since K is zero-indexed.
'''
#!/bin/python3

def sortingCriteria(arr):
    return arr[k]

def athleteSort(athleteList): # global?
    athleteList.sort(key=sortingCriteria)
    return athleteList


if __name__ == '__main__':

    nm = input().rstrip().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for x in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().rstrip())

    result = athleteSort(arr)

    for athlete in result:
        print(' '.join(map(str, athlete)))
