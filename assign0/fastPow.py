def fastPow(b, k):
    if k == 0:
        return 1
    elif k == 1:
        return b
    else:
        return fastPow(b, k-2) * b * b


b = 2
k = 8
print("fastPow(" + str(b) + ", " + str(k) + ") = " + str(fastPow(b, k)))
