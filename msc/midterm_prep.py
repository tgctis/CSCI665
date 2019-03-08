def get_array():
    return [3, 50, 60, 5, 10, 18, 20, 70, 30, 40, 80, 90]


# Insertion Sort #
def i(x, a):
    if len(a) < 1:
        return [x]

    y = a.pop(0)
    if x <= y:
        return [x] + [y] + a
    else:
        return [y] + i(x, a)


def iSort(xs):
    if len(xs) < 1:
        return []
    x = xs.pop(0)
    return i(x, iSort(xs))


a = iSort(get_array())

print a



