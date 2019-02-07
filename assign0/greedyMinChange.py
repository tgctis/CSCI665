def min(m, n):
    if m > n:
        return n
    else:
        return m


def greedyMinChange(a, ds):
    if a == 0:
        return 0
    elif len(ds) < 1:
        return 1000
    else:
        d = ds.pop(0)
        if d > a:
            return greedyMinChange(a, ds)
        else:
            q = a/d
            r = a % d
            return q + greedyMinChange(r, ds)


print greedyMinChange(75, [25, 10, 5, 1])