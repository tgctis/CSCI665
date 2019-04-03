# For comparison purposes.
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


a = {}


def fibDyn(n):
    if n < 2:
        a[n] = n
        return n

    if n-2 in a:
        fib2 = a[n-2]
    else:
        a[n-2] = fibDyn(n-2)
        fib2 = a[n-2]

    if n-1 in a:
        fib1 = a[n-1]
        return fib1 + fib2
    else:
        a[n-1] = fibDyn(n-1)
        fib1 = a[n-1]
        return fib1+fib2


# Comparing speeds
# for i in range(60):
#     print fibDyn(i)
#     print fib(i)


