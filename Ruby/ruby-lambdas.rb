#problem https://www.hackerrank.com/challenges/ruby-lambdas/problem
#points 30

#!Question
#Lambdas

# Lambdas are anonymous functions. Lambdas in Ruby are objects of the class Proc.
# They are useful in most of the situations where you would use a proc.

# The simplest lambda takes no argument and returns nothing as shown below:

# Example:

# #Ruby version <= 1.8
#     lambda { .... } 

#     lambda do
#         ....
#     end

# #Ruby version >= 1.9, "stabby lambda" syntax is added
#     -> { .... }

#     -> do
#         ....
#     end
# Ruby version  can use both lambda and stabby lambda, ->.

# Lambdas can be used as arguments to higher-order functions. They can also be used to construct the result of a higher-order function that needs to return a function.

# Example:

# (a). Lambda that takes no arguments.

# def area (l, b)
#    -> { l * b } 
# end

# x = 10.0; y = 20.0

# area_rectangle = area(x, y).call
# area_triangle = 0.5 * area(x, y).()

# puts area_rectangle     #200.0
# puts area_triangle      #100.0
# (b). Lambda that takes one or more arguments.

# area = ->(a, b) { a * b }

# x = 10.0; y = 20.0

# area_rectangle = area.(x, y)
# area_triangle = 0.5 * area.call(x, y)

# puts area_rectangle     #200.0
# puts area_triangle      #100.0    
# In the above example, we can see that lambdas can be called using both .call() and .().

# Is there any difference between lambdas and procs?
# Yes, there is difference between a proc and a lambda in Ruby.

# Task

# You are given a partially complete code. Your task is to fill in the blanks (______).
# There are  variables defined below:

# square is a lambda that squares an integer.
# plus_one is a lambda that increments an integer by .
# into_2 is a lambda that multiplies an integer by .
# adder is a lambda that takes two integers and adds them.
# values_only is a lambda that takes a hash and returns an array of hash values.



# Write a lambda which takes an integer and square it
square      = ->(a) { a * a }

# Write a lambda which takes an integer and increment it by 1
plus_one    = ->(a) { a + 1 }

# Write a lambda which takes an integer and multiply it by 2
into_2      = ->(a) { a * 2 }

# Write a lambda which takes two integers and adds them
adder       = ->(a, b) { a + b }

# Write a lambda which takes a hash and returns an array of hash values
values_only = ->(a) { a.values }


input_number_1 = gets.to_i
input_number_2 = gets.to_i
input_hash = eval(gets)

a = square.(input_number_1); b = plus_one.(input_number_2);c = into_2.(input_number_1); 
d = adder.(input_number_1, input_number_2);e = values_only.(input_hash)

p a; p b; p c; p d; p e
