def iSelect(xs, i):
    return iSelectHelper(xs, i, 0, len(xs)-1)


def p(a, l, h):
    x = a[h]
    i = l-1
    j = l
    while j < h:
        if a[j] <= x:
            i = i+1
            t = a[i]
            a[i] = a[j]
            a[j] = t
        j = j+1
    t = a[i+1]
    a[i+1] = a[h]
    a[h] = t
    return i+1


def iSelectHelper(xs, i, l, g):
    j = p(xs, l, g)

    if i < j:
        return iSelectHelper(xs, i, l, j-1)
    if i > j:
        return iSelectHelper(xs, i, j+1, g)
    else:
        return xs[j]


xs = [0, 2, 7, 9, 55]
i = 1

print iSelect(xs, i)
