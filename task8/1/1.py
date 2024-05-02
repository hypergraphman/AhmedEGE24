from itertools import product
#                                                  7421865930
words = [''.join(word) for word in product(sorted('7421865930'), repeat=5)]
print(words[:10])
k = 0
for word in words:
    if '68930' <= word <= '98390':
        k += 1
print(k)