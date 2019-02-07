def powIt(b, n):
    a = 1
    while(True):
        if n == 0:
            return a
        else:
            a *= b
            n -= 1


print powIt(2, 8)
