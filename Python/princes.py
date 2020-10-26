#!/usr/bin/python
"""
Princess Peach is trapped in one of the four corners of a square grid. You are in the center of the grid and can move one step at a time in any of the four directions. Can you rescue the princess?

Input format

The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid. This is followed by an NxN grid. Each cell is denoted by '-' (ascii value: 45). The bot position is denoted by 'm' and the princess position is denoted by 'p'.

Grid is indexed using Matrix Convention

Output format

Print out the moves you will take to rescue the princess in one go. The moves must be separated by '\n', a newline. The valid moves are LEFT or RIGHT or UP or DOWN.

Sample input

3
---
-m-
p--

Sample output

DOWN
LEFT

Task

Complete the function displayPathtoPrincess which takes in two parameters - the integer N and the character array grid. The grid will be formatted exactly as you see it in the input, so for the sample input the princess is at grid[2][0]. The function shall output moves (LEFT, RIGHT, UP or DOWN) on consecutive lines to rescue/reach the princess. The goal is to reach the princess in as few moves as possible.

The above sample input is just to help you understand the format. The princess ('p') can be in any one of the four corners.

Scoring
Your score is calculated as follows : (NxN - number of moves made to rescue the princess)/10, where N is the size of the grid (3x3 in the sample testcase). 

https://www.hackerrank.com/challenges/saveprincess/problem
"""
def displayPathtoPrincess(n,grid):
    p = [0,0]
    b = [0,0]
    path = []
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 'm':
                b = [row, col]
            if grid[row][col] == 'p':
                p = [row, col]
    # print(p, b)
    # going to the same row
    if p[0] > b[0]:
        path += ["DOWN" for x in range(p[0]-b[0])]
    elif p[0] < b [0]:
        path += ["UP" for x in range(b[0]-p[0])]
    
    # going to the same column
    if p[1] > b[1]:
        path += ["RIGHT" for x in range(p[1]-b[1])]
    elif p[1] < b [1]:
        path += ["LEFT" for x in range(b[1]-p[1])]
    
    for action in path:
        print(action)

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
