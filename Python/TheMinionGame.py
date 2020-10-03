#Kevin and Stuart want to play 'The Minion Game'

#Game Rules

#1) Both players are given the same string, S
#2) Both players have to make substrings using the letters of the string .
#3) Stuart has to make words starting with consonants.
#4) Kevin has to make words starting with vowels.
#5) The game ends when both players have made all possible substrings. 

#Scoring :- A player gets +1 points for each occurance of the substring in the string S

#For Example :- String S = BANANA
#Kevin's vowel beginning word = ANA
#Here's ANA occurs twice in BANANA. Hence, Kevin will get 2 points.

#Input Format :- A single line of input containing the string S. Also, The string S will contain only uppercase letters [A-Z]

#Constratints :- 0 < len(S) < 10 to the power 6

#Output :- Print one line: the name of the winner and their score separated by a space. If the game is a draw, print Draw.

#Sample Input :- BANANA
#Sample Output :- Stuart 12 

def minion_game(string):
    vowel =['A','E','I','O','U']
    S=0
    K=0
    for i in range(len(string)):
        if string[i] in vowel:
            K+= len(string)-i
        else:
            S+=len(string)-i
    if S>K:
        print("Stuart"+" "+ "%d" % S)
    elif K>S:
        print("Kevin"+" "+'%d' % K)
    else:
        print("Draw")

#Note :- The Answer is to put directly in the compiler (Any Python compiler)