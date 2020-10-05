Problem
You are required to enter a word that consists of x and y that denote the number of Zs and Os respectively. The input word is considered similar to the word zoo if 2×x=y. Determine if the entered word is similar to the word zoo.

For example, words such as zzoooo and zzzoooooo are similar to the word zoo but not the words such as zzooo and zzzooooo.

Input format

First line: A word that starts with several Zs and continues by several Os.

Note: The maximum length of this word must be 20.

Output format

Print Yes if the input word can be considered as the string zoo otherwise, print No.

SAMPLE INPUT  

zzzoooooo

SAMPLE OUTPUT  

Yes

 

PYTHON PROGRAM
x='z'

y='o'

r=str(input())

if r.count(y)/r.count(x)==2:

  print('Yes')

else:

  print('No')

