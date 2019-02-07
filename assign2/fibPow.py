def L(a, b):
    return b, a+b


def fibPow(i, k):
    a = i[0]
    b = i[1]
    if k == 0:
        return a
    elif k == 1:
        return b
    else:
        return fibPow(L(b, a+b), k-2)


for i in range(1, 30):
    print fibPow([1, 0], i)

print "Time complexity = O(log(n))"
