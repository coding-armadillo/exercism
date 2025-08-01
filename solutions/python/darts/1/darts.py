def score(x, y):
    d2=x**2+y**2
    if d2>100:
        return 0
    elif d2>25:
        return 1
    elif d2>1:
        return 5
    else:
        return 10
