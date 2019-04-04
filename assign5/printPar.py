import sys


def extraSpace(S, M, i, j):
    if len(S) < 1 or i > j or i >= len(S):
        return M
    return extraSpace(S, M-(len(S[i])+1), i+1, j)


def badnessLine(S, M, i, j):
    M = extraSpace(S, M, i, j)
    if M < 0:
        return sys.maxint
    return M


def minBad(S, M, i):
    j = i
    while j < len(S) and extraSpace(S, M, i, j) >= 0:
        j += 1
    if extraSpace(S, M, i, len(S)-1) >= 0:
        # print j, S[i:j], badnessLine(S[i:], M, 0, len(S[i:]) - 1)
        return badnessLine(S[i:j], M, 0, len(S)-1)
    # print j, S[i:j], badnessLine(S[i:j], M, 0, j-i-1)
    return badnessLine(S[i:j], M, 0, j-i-1) + minBad(S, M, j)


L = []
def minBadDynamic(S, M):
    if len(S) == 0:
        badness = 0
        for l in L:
            badness += l
        return badness
    i = 0
    j = i
    while j < len(S) and extraSpace(S, M, i, j) >= 0:
        j += 1
    L.append(badnessLine(S[i:j], M, 0, len(S[i:j])))
    return minBadDynamic(S[j:], M)


def minBadDynamicChoice(S, M):
    if len(S) == 0:
        badness = 0
        choices = []
        for l in L:
            badness += l[0]
            choices.append(l[1])
        return badness, choices
    i = 0
    j = i
    while j < len(S) and extraSpace(S, M, i, j) >= 0:
        j += 1
    L.append([badnessLine(S[i:j], M, 0, len(S[i:j])), j])
    return minBadDynamicChoice(S[j:], M)


def printParagraph(S, M):
    lines = minBadDynamicChoice(S, M)
    i = 0
    for l in lines[1]:
        j = i + l
        line = ""
        for n in range(i, j):
            line += S[n] + " "
        print line
        i = j
    print "Line length: %d, Paragraph Badness: %d" % (M, lines[0])


def runner():
    # S = ["My Spoon is too big."]
    S = ["John", "Cleese", "Eric", "Idle", "King Aurthur"]
    M = 15
    printParagraph(S, M)


runner()
