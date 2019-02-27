import sys


def sortedHasSum(a, v):
    l = 0
    h = len(a) - 1
    if v < a[0]:
        return False
    # Trim the list, linear, O(n)
    for i in range(len(a)):
        x = a[i]
        if x > v:
            h = i
    # Iterates on smaller and smaller list
    while True:
        if l > h:
            return False

        q = a[h] + a[l]
        if q == v:
            return True
        elif q > v:
            h = h - 1
        elif q < v:
            l = l + 1
        else:
            return False


def hasSum(a, v):
    l = sys.maxint
    h = l * -1
    it = 0
    # Load the h/l, O(n)
    it = it + 1
    for x in a:
        if x < l:
            l = x
        if x > h:
            h = x
    while True:
        q = l + h
        if v == q:  # O(1)
            # print "l = " + str(l) + " h = " + str(h) + " \nIterations: " + str(it) + " Array length: " + str(len(a))
            return True
        elif v > q:
            t = l
            l = sys.maxint
            it = it + 1
            for x in a:  # O(n)
                if x < l and x > t:
                    l = x
        elif v < q:
            t = h
            h = sys.maxint * -1
            it = it + 1
            for x in a:  # O(n)
                if x > h and x < t:
                    h = x
        else:
            return False
        if l > h:
            return False


a = [3, 5, 10, 18, 20, 30, 40, 50, 60, 70, 80, 90]
_a = [3, 50, 60, 5, 10, 18, 20, 70, 30, 40, 80, 90]
v = 40

print "sortedHasSum? " + str(sortedHasSum(a, v))

a.reverse()
print "hasSum? " + str(hasSum(a, v))
