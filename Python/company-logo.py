
'''

Company Logo
https://www.hackerrank.com/challenges/most-commons/problem

A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string s, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

google would have it's logo with the letters g, o, e.

Input Format

A single line of input containing the string S.

Constraints

3 < len(S) <= 10^4

Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input 0

aabbbccde

Sample Output 0

b 3
a 2
c 2

Explanation 0

aabbbccde

Here, b occurs 3 times. It is printed first.
Both a and c occur 2 times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

Note: The string S has at least 3 distinct characters.

'''

if __name__ == '__main__':
    s = input().strip("\n").strip()

    char_counts = {}
    for c in s:
        char_counts.setdefault(c, 0)
        char_counts[c] += 1

    count = 0
    for (c, cnt) in sorted(char_counts.items(), key=lambda x: (-x[1], x[0]), reverse=False):
        print(c, cnt)
        count += 1
        if count == 3:
            break