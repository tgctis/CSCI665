import sys

# S[[row,col], [row,col]]
# S = [[10, 100], [100, 5], [5, 50]]
S = [[5, 10], [10, 3], [3, 12], [12, 5], [5, 50], [50, 6]]


def minmul(S):
    n = len(S)
    m = [[0 for x in range(n)] for y in range(n)]
    c = [[0 for x in range(n)] for y in range(n)]
    for l in range(1, n+1):
        # print "l = ", l, " to ", n
        for i in range(0, n-l+1):
            # print "i = ", i, " to ", n-l+1
            j = l+i-1
            # print "j = ", j
            champ = sys.maxint
            for k in range(i, j):
                # print "k = ", k, " to ", j
                p = S[i][0]
                q = S[k][1]
                r = S[j][1]
                # print "p*q*r = ", p*q*r
                temp = m[i][k]+m[k+1][j] + p*q*r
                if temp < champ:
                    champ = temp
                m[i][j] = champ
                c[i][j] = k
    return m[0][n-1], c, m


def maxmul(S):
    n = len(S)
    m = [[0 for x in range(n)] for y in range(n)]
    c = [[0 for x in range(n)] for y in range(n)]
    for l in range(1, n+1):
        # print "l = ", l, " to ", n
        for i in range(0, n-l+1):
            # print "i = ", i, " to ", n-l+1
            j = l+i-1
            # print "j = ", j
            champ = sys.maxint*-1
            for k in range(i, j):
                # print "k = ", k, " to ", j
                p = S[i][0]
                q = S[k][1]
                r = S[j][1]
                # print "p*q*r = ", p*q*r
                temp = m[i][k]+m[k+1][j] + p*q*r
                if temp > champ:
                    champ = temp
                m[i][j] = champ
                c[i][j] = k
    return m[0][n-1], c, m


def genparens(S, c, i, j):
    if i == j:
        return S[i]
    print "(", str(genparens(S, c, i, c[i][j])), str(genparens(S, c, c[i][j]+1, j)),  ")"


m = minmul(S)
m = maxmul(S)
print m[0], genparens(S, m[1], 0, len(S)-1)
print m[2]

