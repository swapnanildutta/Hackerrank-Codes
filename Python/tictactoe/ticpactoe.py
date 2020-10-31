"""
Tic-tac-toe is a pencil-and-paper game for two players, X (ascii value 88) and O (ascii value 79), who take turns marking the spaces in a 3×3 grid.
The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal row wins the game. Empty space is represented by _ (ascii value 95), and the X player goes first.
The function nextMove takes in a char player, and the 3x3 board as an array. Complete the function to print 2 space separated integers r and c which denote the row and column that will be marked in your next move. The top left position is denoted by (0,0).

How does it work?
Your code is run alternately with the opponent bot for every move.

Example input:

X  
___  
___  
_XO  

Example output:

1 0 

Explanation:
The board results in the following state after the above move

___  
X__  
_XO  

Submissions: 3445

Max Score:

10

Difficulty:

Advanced

Rate This Challenge:
More



"""

#!/bin/python3

import random

player = input()
grid = []
for r in range(3):
    grid.append(list(input()))


def random_pos(arr: list):
    rc = len(arr)
    cc = len(arr[0])

    while True:
        r = random.randint(0, rc - 1)
        c = random.randint(0, cc - 1)
        if arr[r][c] == "_":
            break
    return [r, c]


def next_move(grid, user):
    straight_lines = [
        # rows
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        # columns
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        # diagonals
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]]
    ]

    for line in straight_lines:
        # print("line", line)
        score = 0
        cell1xy = line[0]
        cell2xy = line[1]
        cell3xy = line[2]

        cell1 = grid[cell1xy[0]][cell1xy[1]]
        cell2 = grid[cell2xy[0]][cell2xy[1]]
        cell3 = grid[cell3xy[0]][cell3xy[1]]

        if ((cell1 == user or cell1 == '_') and (cell2 == user or cell2 == '_') and (cell3 == user or cell3 == '_')):
            if (cell1 == user):
                score += 1
            if (cell2 == user):
                score += 1
            if (cell3 == user):
                score += 1

            # guarenteed win
            if (score == 2):
                if (cell1 == '_'):
                    return cell1xy, score

                if (cell2 == '_'):
                    return cell2xy, score

                if (cell3 == '_'):
                    return cell3xy, score

            elif (score == 1):
                pass

            elif (score == 0):
                pass
        else:
            pass
    return random_pos(grid), 0


next_move_pos, score = next_move(grid, player)
if score <= 1:
    next_move_pos, score = next_move(grid, 'X' if player == 'O' else 'X')
print(" ".join(map(str, next_move_pos)))
