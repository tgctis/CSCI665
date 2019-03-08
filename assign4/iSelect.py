def iSelect(xs, i):
    return iSelectHelper(xs, i, 0, len(xs))

# Replace with in-place algo from note papers
def p(x, ys=[], l=[], g=[]):
    if len(ys) < 1:
        return [l, g]
    else:
        y = ys.pop()
        if y <= x:
            l.append(y)
            return p(x, ys, l, g)
        elif y > x:
            g.append(y)
            return p(x, ys, l, g)


def iSelectHelper(xs, i, l, g):
    x = xs[l]
    p(x, xs, l, g)
    return l+g


xs = [0, 2, 7, 9, 55]
i = 3

print iSelect(xs, i)
