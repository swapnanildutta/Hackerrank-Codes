"""
Tron is a two player game based on the popular movie Tron. The objective of the game is to cut off players movement through each others motorbikes that leave a wall behind them as they move.

Input Format

This version of Tron takes place on a 15x15 grid. Top left of the grid is (0,0) and the bottom right of the grid is indexed as (14,14).
The 1st player is represented by r (ascii value 114) and is positioned with his bike at (7,1) and the 2nd player is represented by g (ascii value 103) and is positioned with his bike at the opposite end of the grid at (7,13).

The first line contains a character representing the current player.
The second line consists of four single spaced integers representing the current position of the 1st and 2nd players' motorbike.
15 lines follow which represents the grid map.
Boundary is represented by # (ascii value 35), an empty grid is represented by - (ascii value 45). Wall left behind by the player are represented by their respective characters.

Output Format

Player's are allowed to output any one of the following moves as the movement of their motorbikes.

    LEFT
    RIGHT
    UP
    DOWN

all in capital letters.
If (x,y) is the current position of the player's motorbike, then the new position on LEFT would be (x,y-1), RIGHT would be (x, y+1), UP would be (x-1,y) and DOWN would be (x+1,y).

Sample Input

r
4 3 5 13
###############
#-rr--------gg#
#-rr--------gg#
#-rr--------gg#
#-rr--------gg#
#-r---------g-#
#-r---------gg#
#rr----------g#
#-------------#
#-------------#
#-------------#
#-------------#
#-------------#
#-------------#
###############

Sample Output

RIGHT

The grid results in the following state.

###############
#-rr--------gg#
#-rr--------gg#
#-rr--------gg#
#-rrr-------gg#
#-r---------g-#
#-r---------gg#
#rr----------g#
#-------------#
#-------------#
#-------------#
#-------------#
#-------------#
#-------------#
###############

The current player is r whose motor bike is positioned currently at (4,3). Valid moves are DOWN and RIGHT. The player outputs RIGHT.

Note:- At any point during the gameplay, player's aren't allowed to trace back their moves. i.e., a LEFT is not allowed after a RIGHT and vice versa or an UP isn't allowed after a DOWN and vice versa.

Game Play

The game play is simultaneous. Both players get the same board state. If both the players move to the same cell in their next move or both hit the walls, the game is considered a draw. The player who is unable to move loses.

ref: https://www.hackerrank.com/challenges/tron?hr_b=1
"""

# NOTE: THIS IS ONE OF THE MANY APPROACHES FOR THIS PROBLEM, THERE ARE OBIVIOSLY BETTER APPROACHES.

current_player =  input()
player_pos = input().split(" ")
player_pos = list(map(int, player_pos))
rpos = [player_pos[0], player_pos[1]]
gpos = [player_pos[2], player_pos[3]]
grid_size = 15
grid = []
for gr in range(grid_size):
    grid.append(input())
    
# algorithm starts, here we are identifying how many free steps in each directions.
def get_free_grid(grid, pos):
    left = right = up = down = 0
    row, column = pos[0]-1, pos[1]
    while row > 0: # up
        if grid[row][column] == "-":
            up += 1
            row -= 1
        else:
            break
    row, column = pos[0]+1, pos[1]       
    while row < 15: #down
        if grid[row][column] == "-":
            down += 1
            row += 1
        else:
            break
    row, column = pos[0], pos[1]+1
    while column < 15: #right
        if grid[row][column] == "-":
            right += 1
            column += 1
        else:
            break
    row, column = pos[0], pos[1]-1
    while column > 0: # left
        if grid[row][column] == "-":
            left += 1
            column -= 1
        else:
            break
    return {"LEFT":left, "RIGHT":right, "UP":up, "DOWN":down}

max_free_direction = ""
max_free_value = 0
ppos = rpos if current_player == "r" else gpos
free_grids = get_free_grid(grid, ppos)

for direction in free_grids:
    if free_grids[direction] > max_free_value:
        max_free_direction, max_free_value = direction, free_grids[direction]
print(max_free_direction)
