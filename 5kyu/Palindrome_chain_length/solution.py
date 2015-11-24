def palindrome_chain_length(n):
    c = 0
    while(1):
        rev = str(n)[::-1]
        if rev == str(n):
            return c
        n += int(rev)
        c += 1
