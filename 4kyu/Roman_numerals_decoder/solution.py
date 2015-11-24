def solution(s):
    ns = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    return (int(ns[s[-1]]) + sum(-1 * ns[c] if ns[s[i + 1]] > ns[c] else
                                      ns[c] for i, c in enumerate(s[:-1])))
