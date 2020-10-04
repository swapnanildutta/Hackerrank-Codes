"""
Given an integer n = 4, the output should be

   #
  ##
 ###
####

ref: https://www.hackerrank.com/challenges/staircase/problem
"""

function staircase(size = nothing,builder = nothing, pad_char = nothing)
    """
    The method takes the size, builder and padding character of a staircase
    and prints the result to console
    if size is not provided, size is defaulted to 6
    if builder is not provided, defaulted to #
    if pad_char is not provided, defaulted to ' ', white space
    """
    
    # check if values are not provided and assign appropriate defaults
    size = (size === nothing) ? 6 : size
    builder = (builder === nothing) ? "#" : builder
    pad_char = (pad_char === nothing) ? " " : pad_char

    # Julia is 1-index based, this means from 1 to size
    # for example, for size = 6, we get 1,2,3,4,5,6
    for loop in 1:size
        # print line to console, pad white spaces and then builder
        println(join([pad_char for lp in 1:(size-loop)]),join([builder for rl in 1:loop]))
    end
end

# printing an empty line
println() # printing an empty line at the end, to look nice
staircase(9)
println() # printing an empty line at the end, to look nice