#Marc loves cupcakes, but he also likes to stay fit. Each cupcake has a calorie count, and Marc can walk a distance to expend those calories. If Marc has eaten j cupcakes so far, after eating a cupcake with  calories he must walk at least 2^j * c miles to maintain his weight.

#For example, if he eats 3 cupcakes with calorie counts in the following order: [5,10,7], the miles he will need to walk are 2^0 * 5 + 2^1 * 5 + 2^2 * 7 = 5+20+28 = 53. This is not the minimum, though, so we need to test other orders of consumption. In this case, our minimum miles is calculated as 2^0 * 10 + 2^1 * 7 + 2^2 * 5 = 10+14+20 = 44.

#Given the individual calorie counts for each of the cupcakes, determine the minimum number of miles Marc must walk to maintain his weight. Note that he can eat the cupcakes in any order.

#Function Description:

#Complete the marcsCakewalk function in the editor below. It should return a long integer that represents the minimum miles necessary.

#marcsCakewalk has the following parameter(s):
#calorie: an integer array that represents calorie count for each cupcake

#Input Format
#The first line contains an integer , the number of cupcakes in .
#The second line contains  space-separated integers .

#Constraints
#1<=n<=40
#1<=c[i]<1000

#Output Format
#Print a long integer denoting the minimum number of miles Marc must walk to maintain his weight.

#Sample Input 0
#3
#1 3 2

#Sample Output 0
#11

#!/bin/python3

import os

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    summ=0
    length = len(calorie)
    for i in range(length-1,-1,-1):
        summ+=calorie[i]*pow(2,i)
    return summ
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
