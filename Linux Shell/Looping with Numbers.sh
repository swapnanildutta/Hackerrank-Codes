#Use a for loop to display the natural numbers from 1 to 50.

#Input Format

#There is no input

#Output Format

#1
#2
#3
#4
#5
#.
#.
#50

#!/bin/bash

X=1
while [ $X -le 50 ]
do
        echo $X
        X=$((X+1))
done

