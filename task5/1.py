def f(n):
    s1 = sum(map(int, [x for x in str(n) if x in '02468']))
    s2 = sum(map(int, str(n)[1::2]))
    return abs(s1 - s2)


def f2(n):
    s1 = 0
    for x in str(n):
        if x in '02468':
            s1 += int(x)
    s2 = 0
    for x in str(n)[1::2]:
        s2 += int(x)
    return abs(s1 - s2)


n = 1
while f2(n) != 17:
    n += 1
print(n)
