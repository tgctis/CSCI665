def prodAccum(m, n, a):
    if m == 0:
        return a
    else:
        return prodAccum(m-1, n, a+n)


print ("prodAccum(10, 2, 0) = " + str(prodAccum(10, 2, 0)))
