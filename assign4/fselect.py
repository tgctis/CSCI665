def fselect(xs=[], i=0):
    if len(xs) < 1:
        return False
    x = xs[0]
    l = []
    s = []
    g = []
    for y in xs:
        if y < x:
            l.append(y)
        elif y > x:
            g.append(y)
        else:
            s.append(y)

    if i < len(l):
        return fselect(l, i)
    elif i >= (len(l) + len(s)):
        return fselect(g, i-(len(l) + len(s)))
    elif len(l) <= i <= (len(l) + len(s)):
        return x
    return i


a = [0, 2, 7, 9, 55]
i = 3

print fselect(a, i)
