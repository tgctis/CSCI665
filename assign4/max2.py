def max2(x, y):
    r = 0
    while x or y:
        if x:
            x = x-1
        if y:
            y = y-1
        r = r+1
    return r


print max2(5, 8)
