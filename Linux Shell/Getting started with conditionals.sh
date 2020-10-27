# Read in one character from STDIN.
# If the character is 'Y' or 'y' display "YES".
# If the character is 'N' or 'n' display "NO".
# No other character will be provided as input.

# Input Format

# One character

# Output Format

# echo YES or NO to STDOUT.

#!/bin/bash

read c
[[ "$c" == [yY] ]] && echo "YES" || echo "NO"
