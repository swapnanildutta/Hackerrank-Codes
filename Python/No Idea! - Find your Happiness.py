'''
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if i ∈ A, you add 1 to your happiness. If i ∈ B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints

1 <= n <= 10^5
1 <= n <= 10^5
1 <= Any integer in the inputs <= 10^9

Input Format

The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7

Sample Output

1

Explanation

You gain 1 unit of happiness for elements 3 and 1 in set A. You lose 1 unit for 5 in set B. The element 7 in set B does not exist in the array so it is not included in the calculation.
Hence, the total happiness is 2 - 1 = 1.
'''

if __name__ == '__main__':
  n,m=[int(i) for i in input().split(" ")]

  n1=[int(i) for i in input().split(" ")]

  a=set([int(i) for i in input().split(" ")])

  b=set([int(i) for i in input().split(" ")])
  happiness=0
  for j in n1:
    if j in a:
      happiness+=1
    if j in b:
      happiness-=1
print(happiness)
