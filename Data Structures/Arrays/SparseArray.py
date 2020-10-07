def matchingStrings(strings, queries):
    reslis=[]
    for x in queries:
        count=0
        if x in strings:
            count=strings.count(x)
        reslis.append(count)
    return reslis        

if __name__ == '__main__':
    
    strings_count = int(input())
    strings = []
    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())
    queries = []
    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)
    print(res)
