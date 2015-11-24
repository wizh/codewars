divisors(n):
    divs = []
    for i in range(2, n):
        if n % i == 0:
            divs.append(i)
    return divs if len(divs) > 0 else ('%d is prime' % n)
