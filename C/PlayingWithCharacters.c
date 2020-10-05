# https://www.hackerrank.com/challenges/playing-with-characters/problem
# Input a character,string and sentence and print it


# Task

# You have to print the character, ch, in the first line. Then print  in next line. In the last line print the sentence sen, .

#Input Format

#First, take a character, ch as input.
#Then take the string,s as input.
#Lastly, take the sentence sen as input.

#Constraints

#Strings for s and sen will have fewer than 100 characters, including the newline.

#Output Format

#Print three lines of output. The first line prints the character, ch.
#The second line prints the string, s.
#The third line prints the sentence, sen.



#include<stdio.h>

int main(){

    char c;
    char s[100];
    char string[100];

    scanf("%c",&c);
    scanf("%s",s);
    scanf("\n");
    scanf("%[^\n]%*c",string);



    printf("%c\n",c);
    puts(s);
    puts(string);

}
