
'''

Apples and Oranges
https://www.hackerrank.com/challenges/apple-and-orange/problem

'''

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    a_cnt = 0
    o_cnt = 0
    for apl in apples:
        if in_range(apl + a, s, t):
            a_cnt = a_cnt + 1
    
    for ong in oranges:
        if in_range(ong + b, s, t):
            o_cnt = o_cnt + 1

    print(a_cnt)
    print(o_cnt)


def in_range(a, b, c):
    return a >= b and a <= c

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
