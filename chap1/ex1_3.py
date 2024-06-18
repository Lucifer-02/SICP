def f(a, b, c):
    if a >= b:
        if b >= c:
            return a * a + b * b
        else:
            return a * a + c * c
    else:
        if a <= c:
            return b * b + c * c
