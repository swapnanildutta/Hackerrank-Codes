#Answer to the challenge "String split and Join" in Python3

#In Python, a string can be split on a delimeter. Example
#>>> a = "this is a string"
#>>> a = a.split(" ") # a is converted to a list of strings. 
#>>> print a
#['this', 'is', 'a', 'string']

#joining a string is simple :

#>>> a = "-".join(a)
#>>> print a
#this-is-a-string 

#Task :- You are given a string. Split the string on a " "(space)delimeter and join using a - hyphen

#input Format :- The first line contains a string consisting of space separated words.

#output Format:- Print the formatted string as explained above 

#Sample input :- this is a string.

#sample output:- this-is-a-string

#the code to be written directly in a compiler.

print('-'.join(input().split()))

