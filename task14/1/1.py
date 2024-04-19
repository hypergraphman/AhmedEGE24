import string


def n_to_p(n, p):
    alp = '0123456789' + string.ascii_uppercase
    r = ''
    while n:
        r = alp[n % p] + r
        n //= p
    return r


print(n_to_p(8 ** 5 + 4 ** 5 - 16, 2).count('1'))