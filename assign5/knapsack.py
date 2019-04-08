W = 15
I = []
K = []
# I.append((1, 16))
I.append((1, 15))
I.append((10, 2))
I.append((10, 2))
I.append((10, 2))
I.append((10, 2))
I.append((15, 4))
I.append((5, 1))


def knapsack(I, W):
    n = len(I)
    if W <= 0 or n < 1:
        return W
    v = 0
    for i in range(0, n):
        v = I[i][0]
        w = I[i][1]
        if w <= W:
            I.pop(i)
            K.insert(W, [v, w])
            W -= w
            # print "Inserting item %d weighs %d and has a value of %d. Knapsack left = %d " % (i, w, v, W)
            break
    return v + knapsack(I, W)


# print "Knapsack(I, W), K"
print "Knapsack value: %d, Contents: " % knapsack(I, W), K
# print "Knapsack Contents(I, W), K: "


def knapsackContents(I, W):
    n = len(I)
    if W <= 0 or n < 1:
        return W
    win_ratio = -1
    win_w = -1
    win_v = -1
    win_i = -1
    for i in range(0, n):
        v = I[i][0]
        w = I[i][1]
        ratio = (v * 1.0)/(w * 1.0)
        if w <= W and ratio > win_ratio:
            win_i = i
            win_v = v
            win_w = w
    if win_i >= 0:
        I.pop(win_i)
        K.insert(W, [win_v, win_w])
        W -= win_w
        # print "Inserting item %d weighs %d and has a value of %d. Knapsack left = %d " % (win_i, win_w, win_v, W)
        return win_v + knapsackContents(I, W)
    return 0


print "KnapsackContents value = %d, Contents: " % knapsackContents(I, W), K
