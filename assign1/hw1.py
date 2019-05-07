def fib(n):  # Slows down around fib(28)
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


# for i in range(0, 100):
#     print str(i) + " : " + str(fib(i))


def fibItHelper(n, a, b):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibItHelper(n-1, b, a+b)


def fibIt(n):
    return fibItHelper(n, 0, 1)


for i in range(0, 100):  # Much faster!
    print str(i) + " : " + str(fibIt(i))
#
# print fibIt(5)  # fast
# print fib(30)  # slow

