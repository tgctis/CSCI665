def max(_arr, m):
    arr = _arr[:]
    if len(arr) == 0:
        return m
    else:
        x = arr.pop()
        if m > x:
            return max(arr, m)
        else:
            return max(arr, x)


def min(_arr, m):
    arr = _arr[:]
    if len(arr) == 0:
        return m
    else:
        x = arr.pop()
        if m < x:
            return min(arr, m)
        else:
            return min(arr, x)


def minI(_arr, n, i, j):
    arr = _arr[:]
    if len(arr) == 0:
        return i - 1, n
    else:
        j += 1
        x = arr.pop(0)
        if n < x:
            return minI(arr, n, i, j)
        else:
            return minI(arr, x, j, j)

def ss(arr):
    for i in range(len(arr) - 1, 0, -1):
        mx = 0
        for j in range(1, i+1):
            if arr[j] > arr[mx]:
                mx = j
        tmp = arr[i]
        arr[i] = arr[mx]
        arr[mx] = tmp
    return arr


def s(arr, ret):
    if len(arr) == len(ret):
        return ret
    else:
        ret.append(max(arr, 0))
        return s(arr, ret)


def mins(arr, i):
    if i == len(arr):
        return arr
    else:
        tmp = arr[i]
        ret = minI(arr, max(arr, 0), 0, 0)
        j = ret[0]
        k = ret[1]
        arr[j] = tmp
        arr[i] = k
        i += 1
        return mins(arr, i)


_arr1 = [3, 2, 1]
_arr = [54,26,93,17,77,31,44,55,20]
# print min(_arr, _arr[0])
# print s(_arr, [])
print minI(_arr, max(_arr, 0), 0, 0)
print mins(_arr, 0)
# print _arr
# print ss(_arr)
