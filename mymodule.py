def intersect_mod(x, y):
    s = set()
    for i in x:
        if i in y:
            s.add(i)
    return s
