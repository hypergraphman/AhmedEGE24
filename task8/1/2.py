from itertools import product

words = [''.join(word) for word in product(sorted('СВЕКЛА'), repeat=5)]

for i, word in enumerate(words, start=1):
    if i == 595:
        print(i, word)