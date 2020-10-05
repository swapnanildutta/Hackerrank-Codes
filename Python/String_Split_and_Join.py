"""
In Python, a string can be split on a delimiter.

Example:

>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings.
>>> print a
['this', 'is', 'a', 'string']

Joining a string is simple:

>>> a = "-".join(a)
>>> print a
this-is-a-string

Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Input Format
The first line contains a string consisting of space separated words.

Output Format
Print the formatted string as explained above.

Sample Input

this is a string

Sample Output

this-is-a-string

"""

def split_and_join(line):
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result
