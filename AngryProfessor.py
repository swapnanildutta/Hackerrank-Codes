if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        n, m = map(int, raw_input().split())
        A = map(int, raw_input().split())
        for x in A:
            if x <= 0:
                m -= 1
        if m <= 0:
            print "NO"
        else:
            print "YES"
