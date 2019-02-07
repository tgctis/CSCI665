def prod(m, n):
    if m <= 0:
        return 0
    return prod(m - 1, n) + n


print prod(6, 5)
