def luck_check(s): 
    if len(s) % 2 == 1:
        s = s[:len(s)//2] + s[len(s)//2 + 1:]
    return (sum(int(i) for i in s[:len(s)//2]) == sum(int(i)
				       for i in s[len(s)//2:]))
