# Given three integers (X, Y, and Z) representing the three sides of a triangle, identify whether the triangle is scalene, isosceles, or equilateral.

# If all three sides are equal, output EQUILATERAL.
# Otherwise, if any two sides are equal, output ISOSCELES.
# Otherwise, output SCALENE.
# Input Format

# Three integers, each on a new line.

# Output Format

# One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded).

#!/bin/bash

read c1
read c2
read c3
if [[ $c1 == $c2 && $c2 == $c3 ]] 
then
    echo "EQUILATERAL"
elif [[ $c1 == $c2 || $c2 == $c3 || $c1 == $c3 ]]
then 
    echo "ISOSCELES"
else
    echo "SCALENE"
fi
