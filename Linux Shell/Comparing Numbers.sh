#Given two integers,  and , identify whether  or  or .

#Exactly one of the following lines:
#- X is less than Y
#- X is greater than Y
#- X is equal to Y

#Input Format

#Two lines containing one integer each (X and Y, respectively).

#Output Format

#Exactly one of the following lines:
#- X is less than Y
#- X is greater than Y
#- X is equal to Y

#!/bin/bash

read firstNumber
read secondNumber
if (($firstNumber > $secondNumber)); then
    echo X is greater than Y;
elif (($firstNumber < $secondNumber)); then
    echo X is less than Y;
else
    echo X is equal to Y;
fi

