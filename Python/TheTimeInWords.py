'''
Given the time in numerals we may convert it into words, as shown below:

5:00 -> five o'clock
5:01 -> one minute past five
5:10 -> ten minutes past five
5:15 -> quarter past five
5:30 -> half past five
5:40 -> twenty minutes to six
5:45 -> quarter to six
5:47 -> quarter to six
5:28 -> twenty eight minutes past five

At , use o' clock. For , use past, and for  use to. Note the space between the apostrophe and clock in o' clock. Write a program which prints the time in words for the input given in the format described.

Below is the python program for the same

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# The timeInWords function below.
def timeInWords(hour, minutes):
    text = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "quarter",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        21: "twenty one",
        22: "twenty two",
        23: "twenty three",
        24: "twenty four",
        25: "twenty five",
        26: "twenty six",
        27: "twenty seven",
        28: "twenty eight",
        29: "twenty nine",
        30: "half"
    }
    if minutes == 0:
        return(text[hour] + " o' clock")
    if minutes == 1:
        return(text[minutes] + " minute past " + text[hour])
    if minutes == 15:
        return(text[minutes] + " past " + text[h])
    if minutes < 30:
        return(text[minutes] + " minutes past " + text[hour])
    if minutes == 30:
        return(text[minutes]+" past " + text[hour])
    if hour == 12:
        hour = 1
    else:
        hour = hour + 1
    if minutes == 59:
        return(text[60 - minutes]+" minute to "+text[hour])
    if minutes == 45:
        return(text[60 - minutes] + " to " + text[hour])
    return(text[60 - minutes] + " minutes to " + text[hour])
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
