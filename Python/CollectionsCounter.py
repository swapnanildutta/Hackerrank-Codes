'''
collections.Counter()
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

Sample Code

>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]

Task

is a shoe shop owner. His shop has number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are number of customers who are willing to pay

amount of money only if they get the shoe of their desired size.

Your task is to compute how much money

earned.

Input Format

The first line contains
, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next lines contain the space separated values of the desired by the customer and

, the price of the shoe.

Constraints




Output Format

Print the amount of money earned by

.

Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output

200

Explanation

Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.

Total money earned =

'''

from collections import Counter
if __name__ == '__main__':
    n = int(input())
    l = list(map(lambda x: int(x),input().split()))
    t = int(input())
    tup=list()
    for i in range(t):
        tup.append(tuple(map(lambda x: int(x),input().split())))
total=0
c=dict(Counter(l).items())
for item in tup:
    try:
        if c[item[0]]>0:
            c[item[0]]-=1
            total+=item[-1]
    except:
        pass

print(total)