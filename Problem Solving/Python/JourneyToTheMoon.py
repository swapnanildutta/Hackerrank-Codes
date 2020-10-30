"""
The member states of the UN are planning to send  people to the moon. They want them to be from different countries. You will be given a list of pairs of astronaut ID's. Each pair is made of astronauts from the same country. Determine how many pairs of astronauts from different countries they can choose from.

For example, we have the following data on 2 pairs of astronauts, and 4 astronauts total, numbered  through .

1   2
2   3
Astronauts by country are  and . There are  pairs to choose from:  and .

Function Description

Complete the journeyToMoon function in the editor below. It should return an integer that represents the number of valid pairs that can be formed.

journeyToMoon has the following parameter(s):

n: an integer that denotes the number of astronauts
astronaut: a 2D array where each element  is a  element integer array that represents the ID's of two astronauts from the same country
Input Format

The first line contains two integers  and , the number of astronauts and the number of pairs.
Each of the next  lines contains  space-separated integers denoting astronaut ID's of two who share the same nationality.

Constraints

Output Format

An integer that denotes the number of ways to choose a pair of astronauts from different coutries.

Sample Input 0 :
5 3
0 1
2 3
0 4

Sample Output 0 : 6

Explanation 0:
Persons numbered [0, 1, 4] belong to one country, and those numbered [2, 3] belong to another. The UN has 6 ways of choosing a pair:
[0, 2], [0, 3], [1, 2], [1, 3], [4, 2], [4, 3]

Sample Input 1:
4 1
0 2

Sample Output 1: 5

Explanation 1:
Persons numbered [0, 2] belong to the same country, but persons 1 and 3 don't share countries with anyone else. The UN has 5 ways of choosing a pair:

[0, 1], [0, 3], [1, 2], [1, 3], [2, 3]


"""

import math
import os
import random
import re
import sys

# Complete the journeyToMoon function below.
def journeyToMoon(n, astronaut):
    graph = [[] for i in range(n)]
    for u, v in astronaut:
        graph[u].append(v)
        graph[v].append(u)
    def bfs(source):
        q = [source]
        while q:
            s = q.pop()
            count[0] += 1
            for child in graph[s]:
                if not vis[child]:
                    vis[child] = 1
                    q.append(child)
    vis = [0] * n
    prod = []
    for i in range(n):
        if not vis[i]:
            count = [0]
            vis[i] = 1
            bfs(i)
            prod.append(count[0])
    answer = 0
    pref = prod[:]
    for i in range(len(prod)-2, -1, -1):
        pref[i] += pref[i+1]
    for i in range(len(prod)-1):
        answer += prod[i] * pref[i+1]
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
