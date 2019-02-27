

def p(x, ys=[], l=[], g=[]):
    if len(ys) < 1:
        return [l, g]
    else:
        y = ys.pop()
        if y <= x:
            l.append(y)
            # print x, ys, l, g
            return p(x, ys, l, g)
        elif y > x:
            g.append(y)
            # print x, ys, l, g
            return p(x, ys, l, g)


def quicksort(xs=[]):
    if len(xs) < 1:
        return []
    else:
        x = xs.pop(0)
        lg = p(x, xs, [], [])
        return quicksort(lg[0]) + [x] + quicksort(lg[1])


a = [3, 50, 60, 5, 10, 18, 20, 70, 30, 40, 80, 90]
print quicksort(a)
