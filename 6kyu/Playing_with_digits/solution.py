def dig_pow(n, p):
    res = sum(int(c) ** (p + i) for i, c in enumerate(str(n), 0))
    return res / n if res % n == 0 else -1
