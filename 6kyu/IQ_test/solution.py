def iq_test(l):
    l = [int(x) % 2 for x in l.split(' ')]
    return l.index(1) + 1 if l.count(0) > l.count(1) else l.index(0) + 1
