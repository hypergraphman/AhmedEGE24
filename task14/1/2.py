print(bin(2**2025 + 4**2024 - 2**2023)[2:].count('0'))

import string


def n_to_p(n, p):
    alp = '0123456789' + string.ascii_uppercase
    r = ''
    while n:
        r = alp[n % p] + r
        n //= p
    return r


print(n_to_p(2**2025 + 4**2024 - 2**2023, 2).count('0'))