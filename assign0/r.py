def r(arr):
    ret = []
    while len(arr) > 0:
        ret.append(arr.pop())

    return ret


_arr = [1, 2, 3]
print 'original: '
print _arr
print '\nnew: '
print r(_arr)
