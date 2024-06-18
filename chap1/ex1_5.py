def p():
    return p()


def test(x, y):
    return 0 if x == 0 else y


test(0, p())
