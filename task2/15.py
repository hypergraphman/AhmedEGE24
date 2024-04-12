print("x y z w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if (y == (x or z)) and (((not y) == w) <= ((not w) <= (not z))):
                    print(x, y, z, w)
