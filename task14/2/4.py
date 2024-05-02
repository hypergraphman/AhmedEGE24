for x in range(0, 24):
    f = True
    for y in range(0, 24):
        a = int('3003', 24) + y * 24**1 + x * 24**2
        b = int('1031', 24) + y * 24**2
        n = a + b
        if n % 5 != 0:
            f = False
            break
    if f:
        y = 7
        a = int('3003', 24) + y * 24 ** 1 + x * 24 ** 2
        b = int('1031', 24) + y * 24 ** 2
        n = a + b
        print(x, n // 5)

