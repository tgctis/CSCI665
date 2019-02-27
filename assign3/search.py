import math


def search(a, v):
    l = 0
    h = len(a)
    while True:
        q = int(l + math.floor((h - l) / 2))
        if l > h:
            return False
        elif v == a[q]:
            return True
        elif v < a[q]:
            h = q - 1
        elif v > a[q]:
            l = q + 1
        else:
            return False


def search_r(a, v):
    return search_help(a, v, 0, len(a)-1)


def search_help(a, v, l, h):
    q = int(l + math.floor((h-l)/2))
    if l > h:
        return False
    elif v == a[q]:
        return True
    elif v < a[q]:
        return search_help(a, v, l, q-1)
    elif v > a[q]:
        return search_help(a, v, q+1, h)
    else:
        return False

# Slow in practice because slicing is a linear time op
# def search_slice(a, v):
#     m = math.floor((len(a)-1)/2)
#     if v == a[m]:
#         return True
#     elif v < a[m]:
#         return search_slice(a[0:m-1], v)
#     elif v > a[m]:
#         return search_slice(a[m+1:], v)
#     else:
#         return False


a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
v = 30
print "Searching for " + str(v) + " recursively in " + str(a) + " returns: " + str(search_r(a, v))
print "Searching for " + str(v) + " in " + str(a) + " returns: " + str(search(a, v))
