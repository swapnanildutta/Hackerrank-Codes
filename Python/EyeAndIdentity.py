'''
Task

Your task is to print an array of size X with its main diagonal elements as 's and 's everywhere else.

Input Format

A single line containing the space separated values of  and .
 denotes the rows.
 denotes the columns.

Output Format

Print the desired X array.

Sample Input

3 3
Sample Output

[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]

 '''

 
import numpy
print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))