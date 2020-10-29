/*
  Original Question: https://www.hackerrank.com/challenges/magic-square-forming/problem

  We define a magic square to be an n x n matrix of distinct positive integers from 1 to n^2
  where the sum of any row, column, or diagonal of length n is always equal to the same number: the magic constant.
  
  You will be given a 3 x 3 matrix s of integers in the inclusive range [1-9].
  We can convert any digit a to any other digit b in the range [1-9] at cost of |a-b|.
  Given s, convert it into a magic square at minimal cost. Print this cost on a new line.

  Note: The resulting magic square must contain distinct integers in the inclusive range [1-9]

  Example
  $s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

  The matrix looks like this:
  5 3 4
  1 5 8
  6 4 2

  We can convert it to the following magic square:
  8 3 4
  1 5 9
  6 7 2

  This took three replacements at a cost of |5-8| + |8-9| + |4-7| = 7

  Function Description

  Complete the formingMagicSquare function in the editor below.

  formingMagicSquare has the following parameter(s):
    int s[3][3]: a 3 x 3 array of integers

  Returns
    int: the minimal total cost of converting the input square to a magic square

  Input Format
    Each of the 3 lines contains three space-separated integers of row s[i]

  Constraints
    s[i][j] is within [1-9]
    
  Sample Input 0
  4 9 2
  3 5 7
  8 1 5

  Sample Output 0
  1

  Explanation 0
  If we change the bottom right value,s[2][2], from 5 to 6 at a cost of |6-5| = 1, s becomes a magic square at the minimum possible cost.

  Sample Input 1 
  4 8 2
  4 5 7
  6 1 6

  Sample Output 1
  4

  Explanation 1
  Using 0-based indexing, if we make
    s[0][1] -> 9 at a cost of |9-8| = 1 
    s[1][0] -> 3 at a cost of |3-4| = 1
    s[2][0] -> 8 at a cost of |8-6| = 2
    then the total cost will be 1 + 1 + 2 = 4
*/



#include <stdio.h>
#include <stdlib.h>

// Flip the square vertically
void flipSquare(char *square)
{
    char *tmp = calloc(3, sizeof(char));
    for (int i = 0; i < 3; i++)
    {
        tmp[i] = square[i];
    }
    square[0] = square[6];
    square[1] = square[7];
    square[2] = square[8];
    square[6] = tmp[0];
    square[7] = tmp[1];
    square[8] = tmp[2];
}
// Rotate the square
void rotateSquare(char *square, char rotation)
{
    char *tmp = calloc(2, sizeof(char));

    //CCW
    if (rotation == 0)
    {
        for (char w = 0; w < 2; w++)
        {
            tmp[w] = square[w];
        }
        square[0] = square[2];
        square[1] = square[5];
        square[2] = square[8];
        square[5] = square[7];
        square[8] = square[6];
        square[7] = square[3];
        square[6] = tmp[0];
        square[3] = tmp[1];
    }
    //CW
    else if (rotation == 1)
    {
        for (char w = 1; w < 3; w++)
        {
            tmp[w - 1] = square[w];
        }
        square[2] = square[0];
        square[1] = square[3];
        square[0] = square[6];
        square[3] = square[7];
        square[6] = square[8];
        square[7] = square[5];
        square[8] = tmp[1];
        square[5] = tmp[0];
    }
}

/*
    Solution inspired by
    Author: @Kevinagin, HackerRank
*/
int formingMagicSquare(int x, int y, int **s)
{
    char exampleSequence[9] = {
        2, 7, 6,
        9, 5, 1,
        4, 3, 8};
    char *ptr = exampleSequence;
    int cost = 0;
    int tmp = 0;
    int counter = 0;

    //Initialize cost
    for (int n = 0; n < 9; n++)
    {
        if (s[(n / 3)][(n % 3)] != exampleSequence[n])
        {
            cost += abs(exampleSequence[n] - s[(n / 3)][(n % 3)]);
        }
    }
    while (1)
    {
        tmp = 0;
        for (int n = 0; n < 9; n++)
        {
            if (s[(n / 3)][(n % 3)] != exampleSequence[n])
            {
                tmp += abs(exampleSequence[n] - s[(n / 3)][(n % 3)]);
            }
        }
        if (tmp < cost)
        {
            cost = tmp;
        }
        rotateSquare(exampleSequence, 0);
        counter++;
        if (counter % 4 == 0)
        {
            flipSquare(exampleSequence);
        }
        if (counter % 8 == 0)
        {
            break;
        }
    }
    return cost;
}
