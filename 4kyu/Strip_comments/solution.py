def solution(s, ms):
    ret = []
    for l in s.split('\n'):
        nl = ''
        for c in l:
            if c in ''.join(ms):
                break
            nl += c
        ret.append(nl.rstrip())
    return '\n'.join(ret)
