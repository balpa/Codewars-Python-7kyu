def modified_sum(a, n):
    pow = [x**n for x in a]
    sumarr = sum(a)
    sumpow = sum(pow)
    return sumpow-sumarr
