"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
s = '12:01:00PM'

Return '12:01:00'.

s = '12:01:00AM'

Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in 12 hour format
Returns

string: the time in 24 hour format
Input Format

A single string  that represents a time in 12-hour clock format (i.e.:hh:mm:ssAM or hh:mm:ssPM).

Constraints

All input times are valid
Sample Input 0

07:05:45PM
Sample Output 0

19:05:45
"""
#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time = s.split(":")
    hour = time[0]
    if hour[0] == 0:
        hour = int(hour[1])
    else:
        hour = int(hour) % 12
    minute = time[1]
    seconds = time[2]
    if "AM" in seconds:
        if len(str(hour)) == 1:
            hour = str(hour)
            hour = "0" + hour
        else:
            hour = str(hour)
        return (hour+":"+minute+":"+seconds[0:2])
    elif "PM" in seconds:
        hour += 12
        return (str(hour)+":"+minute+":"+seconds[0:2])
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
