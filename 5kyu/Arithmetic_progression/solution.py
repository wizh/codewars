def find_missing(l):
    for i in range(len(l) - 2):
        a, b, c = l[i], l[i + 1], l[i + 2]
        gap = min(b - a, c - b)
        if b - a > c - b:
            return a + gap
        elif c - b > b - a:
            return b + gap
    return -1
