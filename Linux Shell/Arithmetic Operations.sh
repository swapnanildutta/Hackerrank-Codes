# A mathematical expression containing +,-,*,^, / and parenthesis will be provided. Read in the expression, then evaluate it. Display the result rounded to 3 decimal places.

# Sample Input 1

# 5+50*3/20 + (19*2)/7

# Sample Output

# 17.929

read p1
read p2
read p3

printf "%.3f\n" `echo $p1 | bc -l`

