"""
Task

Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. 
She decided to count the total number of distinct country stamps in her collection. 
She asked for your help. You pick the stamps one by one from a stack of
n country stamps

Input Format

The first line contains an integer n, the total number of country stamps.
The next n lines contains the name of the country where the stamp is from.

Input Format

The first line contains an integer , the total number of country stamps.
The next  lines contains the name of the country where the stamp is from.

Constraints
0<n<1000


Output Format

Output the total number of distinct country stamps on a single line.

Sample Input
7
UK
China
USA
France
New Zealand
UK
France 

Sample Output
5

Explanation

UK and France repeat twice.
Hence, the total number of distinct country stamps is 5(five).
"""

n=int(input())
s=set()

for i in range(n):
    stamp=input()
    s.add(stamp)

count=0
for i in s:
    count+=1

print(count)