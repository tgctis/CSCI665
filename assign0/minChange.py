def min(m, n):
    if m is None:
        return n
    elif n is None:
        return m

    if m > n:
        return n
    else:
        return m


def minChange(a, ds):
    if a == 0:
        return 0
    elif len(ds) < 1:
        return None
    else:
        d = ds.pop(0)
        if d > a:
            return minChange(a, ds)
        else:
            return min((1 + minChange(a-d, ([d] + ds))), minChange(a, ds))


print minChange(74, [25, 10, 5, 1])
