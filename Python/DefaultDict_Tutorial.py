# This is the working code of Default Dict Tutorial problem at Hackerrank in Python 2.

# The default dict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.
# For example:

#from collections import defaultdict
#d = defaultdict(list)
# d['python'].append("awesome")
#d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#    print i

# This prints :

#('python', ['awesome', 'language'])
#('something-else', ['not relevant'])

# In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group . There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurance of m in group A. If it does not appear , print -1.

# Constrainst :

#1 <= n <= 10000
#1 <= n <= 100
# 1 <= length of each word in the input <=100

# Input Format :-

# The first line contains integers, n and m separated by a space.
# The next n lines contains the words belonging to group A.
# The next m lines contains the words belonging to group B.\

# Output formats:
# Output m lines
# The ith line should contain 1-indexed positions of the occurance of the ith word separated by spaces.

# Sample input:

# 5 2
# a
# a
# b
# a
# b
# a
# b

# Sample Output :
# 1 2 4
# 3 5

# Explanation

# 'a' appeared 3 times in positions 1,2 and 4
# 'b' appeared 2 times in positions 3 and 5.
# In the sample problem, if 'c' also appeared in word group B, you would print -1

from collections import defaultdict
d = defaultdict(list)
list1 = []

n, m = map(int, input().split())

for i in range(0, n):
    d[input()].append(i+1)

    for i in range(0, m):
        list1 = list1+[input()]

        for i in list1:
            if i in d:
                print(" ").join(map(str, d[i]))
            else:
                print -1

# This is the working code. Direct paste in compiler for code. Thank you!
