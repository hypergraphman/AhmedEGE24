for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (((not x and y) <= w) and ((x and y) <= (not z or w))) == 0:
                    print(x, y, w, z)
