import string


def n_to_p(n, p):
    alp = '0123456789' + string.ascii_uppercase
    r = ''
    while n:
        r = alp[n % p] + r
        n //= p
    return r


print(n_to_p(45 * 400 ** 10 - 8 ** 5 * 5 ** 8 + 16 * 20 ** 3 - 33, 20))
