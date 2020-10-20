#When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently.

#There is a list of 26 character heights aligned by index to their letters. For example, 'a' is at index 0 and 'z' is at index 25. There will also be a string. Using the letter heights given, determine the area of the rectangle highlight in mm^2 assuming all letters are 1mm wide.

#Example
#h=[1,3,1,3,1,4,1,3,2,5,5,5,5,1,1,5,5,1,5,2,5,5,5,5,5,5]
#word='torn'
#The heights are t=2, o=1, r=1 and n=1. The tallest letter is 1 high and there are 4 letters. The hightlighted area will be 2*4=8mm^2 so the answer is 8.

#Function Description

#Complete the designerPdfViewer function in the editor below.

#designerPdfViewer has the following parameter(s):

#int h[26]: the heights of each letter
#string word: a string

#Returns

#int: the size of the highlighted area

#Input Format

#The first line contains  space-separated integers describing the respective heights of each consecutive lowercase English letter, ascii[a-z].
#The second line contains a single word consisting of lowercase English alphabetic letters.

#Constraints

#1<=h[?]<=7, where ? is an English lowercase letter.
#word contains no more than  letters.

#Sample input 0
#1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
#abc

#Sample output 0
#9

#Explanation 0
#We are highlighting the word abc:

#Letter heights are a=1, b=3 and c=1. The tallest letter, b, is 3mm high. The selection area for this word is 3*1*1=9mm^2.

#Note: Recall that the width of each character is 1mm.

#!/bin/python3
import os

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    ll=[]
    for el in word:
        ll.append(el)
    print(ll)
    asc=[]
    for i,el in enumerate(ll):
        print(ll[i]," ",ord(ll[i]))
        asc.append(ord(ll[i])-97)
    print(asc)
    chval=[]
    for elm in asc:
        chval.append(h[elm])
    print(chval)
    return len(word)*max(chval)   
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
