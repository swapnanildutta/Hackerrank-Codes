'''
A 10 X 10 Crossword grid is provided to you, along with a set of words (or names of places) which need to be filled into the grid. Cells are marked either + or -. Cells marked with a - are to be filled with the word list.

The following shows an example crossword from the input crossword grid and the list of words to fit, 
words=[POLAND, LHASA, SPAIN, INDIA]:

Input 	   		            Output

++++++++++ 		            ++++++++++
+------+++ 		            +POLAND+++
+++-++++++ 		            +++H++++++
+++-++++++ 		            +++A++++++
+++-----++ 		            +++SPAIN++
+++-++-+++ 		            +++A++N+++
++++++-+++ 		            ++++++D+++
++++++-+++ 		            ++++++I+++
++++++-+++ 		            ++++++A+++
++++++++++ 		            ++++++++++
POLAND;LHASA;SPAIN;INDIA


Function Description

Complete the crosswordPuzzle function in the editor below. It should return an array of strings, each representing a row of the finished puzzle.

crosswordPuzzle has the following parameter(s):

    * crossword: an array of 10 strings of length 10 representing the empty grid
    * words: a string consisting of semicolon delimited strings to fit into crossword

Input Format

Each of the first 10 lines represents crossword[i], each of which has 10 characters, crossword[i][j].

The last line contains a string consisting of semicolon delimited words[i] to fit.

Constraints

    * 1 <= |words| <= 10
    * crossword[i][j] can be either +, X, or -, - represent empty space
    * words[i][j] can only be alphabets lying between A to Z (both included)

Sample Input 0

+-++++++++
+-++++++++
+-++++++++
+-----++++
+-+++-++++
+-+++-++++
+++++-++++
++------++
+++++-++++
+++++-++++
LONDON;DELHI;ICELAND;ANKARA

Sample Output 0

+L++++++++
+O++++++++
+N++++++++
+DELHI++++
+O+++C++++
+N+++E++++
+++++L++++
++ANKARA++
+++++N++++
+++++D++++



Sample Input 1

+-++++++++
+-++++++++
+-------++
+-++++++++
+-++++++++
+------+++
+-+++-++++
+++++-++++
+++++-++++
++++++++++
AGRA;NORWAY;ENGLAND;GWALIOR

Sample Output 1

+E++++++++
+N++++++++
+GWALIOR++
+L++++++++
+A++++++++
+NORWAY+++
+D+++G++++
+++++R++++
+++++A++++
++++++++++



Sample Input 2

XXXXXX-XXX
XX------XX
XXXXXX-XXX
XXXXXX-XXX
XXX------X
XXXXXX-X-X
XXXXXX-X-X
XXXXXXXX-X
XXXXXXXX-X
XXXXXXXX-X
ICELAND;MEXICO;PANAMA;ALMATY
Sample Output 2

XXXXXXIXXX
XXMEXICOXX
XXXXXXEXXX
XXXXXXLXXX
XXXPANAMAX
XXXXXXNXLX
XXXXXXDXMX
XXXXXXXXAX
XXXXXXXXTX
XXXXXXXXYX
'''

# A recursive solution with backtracking

class Space:
    def __init__(self, row, column):
        # Starting Row index
        self.row = row

        #Starting Column index
        self.column = column

        # Length of space or consecutive "-" symbols
        self.length = 0

        # For vertical, I change this to False
        self.horizontal = True

        # Has this space already been used
        self.used = False

    # Just for printing a Space object to Console. Only for debugging
    def __repr__(self):
        direction = "Horizontal"
        if not self.horizontal:
            direction = "Vertical"
        return "Start Index: ({}, {}), Length: {}, Direction: {}".format(self.row, self.column, self.length, direction)

def findAvailableSpaces(grid, minLength):
    spaces=[]
    gridSize = 10
    
    # Horizontal scanning for spaces
    i = 0
    # Loop through all Rows
    while i < gridSize:
        j = 0
        # Loop through all Columns
        while j < gridSize:
            c = grid[i][j]
            if c == "-":
                space = Space(i,j)
                # Count the consecutive "-" symbols
                while j < gridSize and grid[i][j] == "-":
                    space.length += 1
                    j += 1
                # Length of Space should be atleast the size of minimum word to avoid situation like:
                # +++-+++
                # +++-+++
                # +++-+++
                # Here all three "-" are part of a vertical Space not Horizontal
                if space.length >= minLength:
                    spaces.append(space)
            else:
                j += 1
        i += 1

    # Vertical Scanning for spaces
    i = 0
    while i < gridSize:
        j = 0
        while j < gridSize:
            c = grid[j][i]
            if c == "-":
                space = Space(j, i)
                while j < gridSize and grid[j][i] == "-":
                    space.length += 1
                    j += 1
                space.horizontal = False
                if space.length >= minLength:
                    spaces.append(space)
            else:
                j += 1
        i += 1
    return spaces

# To check if the given word can fit the given space
def canFitWord(grid, space, word):
    # If space has already been used by another word
    if space.used:
        return False
    
    for i in range(0, space.length):
        if space.horizontal:
            # We need to check each character along with "-" because of situation like:
            # +++I+++
            # +++N+++
            # ---D---
            # +++I+++
            # +++A+++
            # Here in the third line D is already present
            if grid[space.row][space.column+i] != word[i] and grid[space.row][space.column+i] != '-':
                return False
        else:
            # For vertical words
            if grid[space.row+i][space.column] != word[i] and grid[space.row+i][space.column] != '-':
                return False
    return True

# To fill a word in a Space and return the list of all "-" (row, column) which have been replaced with words
def addWordToGrid(grid, space, word):
    spacesFilled = []
    for i in range(0, space.length):
        if space.horizontal:
            if grid[space.row][space.column+i] == '-':
                spacesFilled.append((space.row, space.column+i))
                grid[space.row][space.column+i]=word[i]
        else:
            if grid[space.row+i][space.column] == '-':
                spacesFilled.append((space.row+i, space.column))
                grid[space.row+i][space.column]=word[i]
    return spacesFilled

# To remove the filled words and replace the cells with "-" again in case the puzzle does not get solved after adding the word
# This may happen when a single word can fit in more than one available Space.
# INDIA can fit in any Space with length 5 but that space may be for DELHI
def removeWordFromGrid(grid, spacesFilled):
    for cell in spacesFilled:
        grid[cell[0]][cell[1]] = "-"

# It recurssively calls itself to fill each word and tries each combiation of word with Space
def solve(grid, spaces, words):
    if len(words) == 0:
        return True

    # Remove the first word from words list
    word = words.pop(0)
    possibleLocations = []

    # List of all spaces which can be fit the word
    for space in spaces:
        if space.length == len(word):
            possibleLocations.append(space)

    # Main recursion happens here
    # It first fits the word in Space and checks if it solves the puzzle.
    # It calls the solve() each time by filling the grid with word until all words fit
    # If at certain point it fails to fit the word, it backtracks and remove the filled words and tries next combination
    for space in possibleLocations:
        if canFitWord(grid, space, word):
            space.used = True
            # Add the word to grid and get list of all filled cells
            filled = addWordToGrid(grid, space, word)
            # Check with recursion to see if our decision to fill was correct
            # If at some point, words can no longer fit, it will back track and move to line after if block below
            if solve(grid, spaces, words):
                return True
            # Failed to solve puzzle. Remove the filled words and mark the Space as not used yet.
            removeWordFromGrid(grid, filled)
            space.used = False

    # Failed to fit the word. Put the word back in the words list
    words.append(word)
    return False

# For preprocessing of data
def crosswordPuzzle(crossword, words):
    words = words.split(";")
    grid = [[s[i] for i in range(10)] for s in crossword]
    minLength = min([len(s) for s in words])
    spaces = findAvailableSpaces(grid, minLength)
    solve(grid, spaces, words)
    return ["".join(s) for s in grid]

crossword = [
    '++++++++++',
    '+------+++',
    '+++-++++++',
    '+++-++++++',
    '+++-----++',
    '+++-++-+++',
    '++++++-+++',
    '++++++-+++',
    '++++++-+++',
    '++++++++++'
]
words = "POLAND;LHASA;SPAIN;INDIA"

solvedPuzzle = crosswordPuzzle(crossword, words)

for i in range(10):
    for j in range(10):
        print(solvedPuzzle[i][j], end="")
    print("\n")