import sys


def extraSpace(S, M, i, j):
    if len(S) < 1 or i > j or i > len(S):
        return M
    # print S[i], len(S[i]) + 1
    return extraSpace(S, M-(len(S[i])+1), i+1, j)


def mn(S, M, i):
    if i > len(S) or extraSpace(S[:i], M, 0, len(S[:i])-1) < 0:
        return i-1
    return mn(S, M, i+1)


def badnessLine(S, M, i, j):
    M = extraSpace(S, M, i, j)
    if M < 0:
        return sys.maxint
    return M


# Not working...
def minBad(S, M, i):
    j = mn(S, M, i)
    for n in range(0, j):
        print S[n],

    if extraSpace(S, M, 0, len(S)-1) >= 0:
        print "| Badness = ", badnessLine(S, M, 0, len(S)-1)
        return badnessLine(S, M, 0, len(S)-1)
    print "| Badness = ", badnessLine(S[:j], M, 0, j - 1)
    return badnessLine(S[:j], M, 0, j-1) + minBad(S[j:], M, 0)


def runner():
    S = ["John", "Cleese", "Eric", "Idle", "King Aurthur"]
    # S = "1", "12", "123"
    M = 15
    i = 0
    print minBad(S, M, i)
    # print mn(S, M, i)

runner()
