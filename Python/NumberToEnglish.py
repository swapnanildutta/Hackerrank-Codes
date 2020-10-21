#
'''
    Problem task: Write a function that accepts a positive integer between 0 and 999 inclusive and returns a string representation of that integer written in English.
    Problem Link: https://edabit.com/challenge/mZqMnS3FsL2MPyFMg
'''

"""
Working
Takes input from Function FormattingNumber() [eg: 123 (type: <int>)]
The input number is converted into String type for better String Manupulation
We intial a result string (String), and a initial string (Dictionary) that contains reference numbers in english

We check if the user input already exists in our dictionary, if so we return the english version [eg: 14 --> fourteen]
### --Taking example as 569-- ####

Otherwise, we first divide all digits in 3 parts that is for (0 - 999) in this case [5 6 9]
We now start from the MSP(Most Significant Place [eg: 5 is MSP in 569])
We get value of 5 from dictionary and append it with string "hundred" and update it in result string
Using dict.get(5)

We do the same for other digits
Keeping in mind the case for occurance of zero
Keeping in mind the case like [519] in which you have to return the value from dictionary itself
"""

def NumToEnglish(num):
    num = str(num)

    resulted_string = ""
    initial_dict = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
                    9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
                    16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
                    40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred"}

    if int(num) in initial_dict.keys():
        return initial_dict.get(int(num))
    else:
        length_of_number = len(num)
        for i in range(length_of_number):
            if i == 0 and int(num[i]) > 0:
                resulted_string = str(initial_dict.get(int(num[i]))) + " " + str(initial_dict.get(100))
            elif i == 1 and int(num[1]) == 1:
                resulted_string = resulted_string + " " + str(initial_dict.get(int(num[1:3])))
            elif i == 1 and int(num[1]) > 1:
                resulted_string = resulted_string + " " + str(initial_dict.get(int(num[1]) * 10))
            elif i == 2 and int(num[1]) != 1 and int(num[i]) > 0:
                resulted_string = resulted_string + " " + str(initial_dict.get(int(num[i])))

    return resulted_string.strip()

"""
converting all the input number in 3 digit numbers [eg: 13 --> 013, 189 --> 189]

working
If the number is of 2 digit add 0 in start of number
No need to code of case (number od digit = 1 ie 0 to 9) as this case will already be added in the dictionary
after conversion the formatted number is passed to Function NumToEnglish()
"""

def FormattingNumber(num):
    num = str(num)
    if len(num) == 2:
        num = "0" + num
    return num

"""
# 't' takes number of test cases as input
# Num is the number input given by the user [eg: 132 (type: <int>)]

# working
# The code takes input (Num) from user and passes it to Function (FormattingNumber() for formatting all number in format abc) [eg: 13 --> 013, 189 --> 189]
"""
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        Num = int(input())
        print(NumToEnglish(FormattingNumber(Num)))
