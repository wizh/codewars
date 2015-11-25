def validBraces(s):
    stack = []
    for c in s:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if len(stack) == 0 or not stack.pop() == '([{'[')]}'.index(c)]:
                return False
    return len(stack) == 0
