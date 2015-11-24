# Obscure, non-understandable, but really cool!
from itertools import chain
def done_or_not(b):
    cs = [[b[j][i] for j in range(9)] for i in range(9)]
    rs = ([[[[b[3 * j + m][3 * i + n] for n in range(3)] for m in range(3)]
                                      for j in range(3)] for i in range(3)])

    rs = ([set(chain(*rs[i][j])) for j in range(3) for i in range(3)])

    return (('Try again!', 'Finished!')
        [all(len(set(x[i])) == 9 for i in range(3) for x in zip(b, cs, rs))])
