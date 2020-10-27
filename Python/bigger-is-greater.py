
'''

Bigger is Greater:
https://www.hackerrank.com/challenges/bigger-is-greater/problem

Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list.

Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:

It must be greater than the original word
It must be the smallest word that meets the first condition
For example, given the word w = abcd, the next largest word is abdc.

Complete the function biggerIsGreater below to create and return the new string meeting the criteria. If it is not possible, return no answer.

Function Description

Complete the biggerIsGreater function in the editor below. It should return the smallest lexicographically higher string possible from the given string or no answer.

biggerIsGreater has the following parameter(s):

w: a string


Input Format

The first line of input contains T, the number of test cases.
Each of the next T lines contains w.

Constraints

1 <= T <= 10^5
1 <= |w| <= 100
w will contain only letters in the range ascii[a..z].


Output Format

For each test case, output the string meeting the criteria. If no answer exists, print no answer.

Sample Input 0

5
ab
bb
hefg
dhck
dkhc

Sample Output 0

ba
no answer
hegf
dhkc
hcdk

Explanation 0

Test case 1:
ba is the only string which can be made by rearranging ab. It is greater.
Test case 2:
It is not possible to rearrange bb and get a greater string.
Test case 3:
hegf is the next string greater than hefg.
Test case 4:
dhkc is the next string greater than dhck.
Test case 5:
hcdk is the next string greater than dkhc.

Sample Input 1

6
lmno
dcba
dcbb
abdc
abcd
fedcbabcd

Sample Output 1

lmon
no answer
no answer
acbd
abdc
fedcbabdc

'''

def swap(a, ix1, ix2):
    tmp = a[ix1]
    a[ix1] = a[ix2]
    a[ix2] = tmp

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    # convert string to list of chars
    chars = list(w)
    # See if we can swap 2 characters, starting at the last character and working forward
    swapped = False
    smallest_ix = len(chars) - 1
    for i in range(len(chars) - 2, -1, -1):
        if chars[i] < chars[i + 1]:
            smallest_char = 'zzz'
            for c_i in range(i+1, len(chars)):
                if chars[c_i] > chars[i] and chars[c_i] < smallest_char:
                    smallest_char = chars[c_i]
                    smallest_ix = c_i

            swap(chars, i, smallest_ix)

            ret_str = chars[:i+1]
            sort_str = chars[i+1:]
            sort_str = sorted(sort_str)
            print(ret_str, sort_str)
            swapped = True
            break

    if not swapped:
        return "no answer"

    return "".join(list(ret_str + sort_str))

if __name__ == '__main__':

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print(result)
