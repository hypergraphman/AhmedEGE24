print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = int(((y <= x) == (x <= w)) and ((not x) <= z))
                if f:
                    print(x, y, z, w)
