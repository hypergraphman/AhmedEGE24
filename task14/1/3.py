import string


def n_to_p(n, p):
    alp = '0123456789' + string.ascii_uppercase
    r = ''
    while n:
        r = alp[n % p] + r
        n //= p
    return r


print(n_to_p(2 * 9 ** 7 - 3 ** 8 - 19, 3).count('2'))
