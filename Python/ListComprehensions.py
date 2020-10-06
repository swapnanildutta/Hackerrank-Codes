'''
Let's learn about list comprehensions! You are given three integers and representing the dimensions of a cuboid along with an integer . You have to print a list of all possible coordinates given by on a 3D grid where the sum of is not equal to . Here,

Input Format

Four integers
and

each on four separate lines, respectively.

Constraints

Print the list in lexicographic increasing order.

Sample Input 0

1
1
1
2

Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Explanation 0

Concept

You have already used lists in previous hacks. List comprehensions are an elegant way to build a list without having to use different for loops to append values one by one. This example might help.

Example: You are given two integers x and y . You need to find out the ordered pairs ( i , j ) , such that ( i + j ) is not equal to n and print them in lexicographic order.( 0 <= i <= x ) and ( 0 <= j <= y) This is the code if we dont use list comprehensions in Python.

python x = int ( raw_input()) y = int ( raw_input()) n = int ( raw_input()) ar = [] p = 0 for i in range ( x + 1 ) : for j in range( y + 1): if i+j != n: ar.append([]) ar[p] = [ i , j ] p+=1 print ar
Other smaller codes may also exist, but using list comprehensions is always a good option. Code using list comprehensions:

python x = int ( raw_input()) y = int ( raw_input()) n = int ( raw_input()) print [ [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )]

Sample Input 1

2
2
2
2

Sample Output 1

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]


'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if(i+j+k)!=n])


If else if ladder in list comprehension 
# Original list of numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# For loop to create a new list where we substitute all multiples of 2 by 0,
# multiples of 3(which are not multiples of 2) by 1 and leave the rest as it is.
modified_numbers = []
for number in numbers:
  if number % 2 == 0:
    modified_numbers.append(0)
  elif number % 3 == 0:
    modified_numbers.append(1)
  else:
    modified_numbers.append(number)
  
# Rewrite using list comprehension.
# Syntax: 
#   list_object = [expression_1_on_item if_condition_1_on_item
#                  else expression_2_on_item if_condition_2_on_item
#                  else expression_3_on_item for_item_in_iterable]
modified_numbers = [0 if number % 2 == 0 else 1 if number % 3 == 0
                    else number for number in numbers]

print(modified_numbers) # Output: [1, 0, 1, 0, 5, 0, 7, 0, 1, 0]
 
