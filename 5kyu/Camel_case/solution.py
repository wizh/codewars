def to_camel_case(s):
    return ('' if not s else s[0] + ''.join(c.upper() if s[::-1][i + 1] in '-_'
                                               else '' if c in '-_'
                                               else c for i, c in
                                               enumerate(s[::-1][:-1]))[::-1])
