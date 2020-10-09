#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    d1 = 0
    d2 = 0

    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if (i == j):
                d1 += arr[i][j]
            if(i == len(arr)-j-1):
                d2 += arr[i][j]
    return abs(d1-d2)
