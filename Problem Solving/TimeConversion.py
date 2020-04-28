'''
Given a time in

-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

    s: a string representing time in 

    hour format

Input Format

A single string
containing a time in -hour clock format (i.e.: or ), where and

.

Constraints

    All input times are valid

Output Format

Convert and print the given time in
-hour format, where

.

Sample Input 0

07:05:45PM

Sample Output 0

19:05:45


'''

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    hr,rest,post=int(s[:2]),s[2:-2],s[-2:]
    if hr==12:
        hr=0
    if post=='PM':
            hr+=12
    hr=str(hr)
    if len(hr)<2:
        hr='0'+hr
    return (hr+rest)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()