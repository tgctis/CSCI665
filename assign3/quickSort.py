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


def quicksort(xs=[], a=[]):
    if len(xs) < 1:
        return a
    else:
        x = xs.pop(0)
        lg = p(x, xs, [], [])
        l = lg[0]
        g = lg[1]
        return quicksort(l, [x] + quicksort(g, a))


a = [3, 50, 60, 5, 10, 18, 20, 70, 30, 40, 80, 90]
print quicksort(a, [])
