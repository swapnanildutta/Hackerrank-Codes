'''
Short Problem Definition:
Marie invented a Time Machine and wants to test it by time-traveling to visit Russia on the Day of the Programmer (the 256th day of the year) during a year in the inclusive range from 1700 to 2700.

Link
Day of The Programmer ( https://www.hackerrank.com/challenges/day-of-the-programmer/problem )

Complexity:
time complexity is O(-1)

space complexity is O(-1)

Execution:
As I have pointed out in the past, no engineer should ever implement any calendar related functions. It should be done natively by the language or by a library.

I am fairly certain that the conventions will change by 2700 🙂 and the calculation will be invalid.

'''

# Solution:

#!/bin/python
 
import math
import os
import random
import re
import sys
 
# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    raise SystemError("This challenge is stupid")
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
 
    year = int(raw_input().strip())
 
    result = dayOfProgrammer(year)
 
    fptr.write(result + '\n')
 
    fptr.close()
