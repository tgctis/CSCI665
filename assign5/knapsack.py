W = 15
I = []
K = []
I.append((1, 16))
I.append((1, 15))
I.append((10, 2))
I.append((10, 2))
I.append((10, 2))
I.append((10, 2))
I.append((15, 4))
I.append((5, 1))


def knapsack(I, W):
    n = len(I)
    c = [[0 for x in range(W)] for y in range(n)]  # blank matrix for calculations, stores knapsack value
    for i in range(0, n):  # for all items
        for w in range(1, W):  # for all weights
            if I[i][1] <= w:  # If the item has a weight less than or equal to the weight for the cell
                champ = c[i-1][w]  # previous item's value at weight
                temp = I[i][0] + c[i-1][w-I[i][1]]  # current item's value
                if temp > champ:  # If the item + knapsack is better than the previous item
                    champ = temp  # put it in the slot
                c[i][w] = champ
    return c[n-1][W-1]


print "Maximum knapsack value: ", knapsack(I, W)


def knapsackContents(I, W):
    n = len(I)
    c = [[0 for x in range(W)] for y in range(n)]  # blank matrix for calculations, stores knapsack value
    K = []
    for i in range(0, n):  # for all items
        for w in range(1, W):  # for all weights
            if I[i][1] <= w:  # If the item has a weight less than or equal to the weight for the cell
                champ = c[i - 1][w]  # previous item's value at weight
                temp = I[i][0] + c[i - 1][w - I[i][1]]  # current item's value
                if temp > champ:  # If the item + knapsack is better than the previous item
                    champ = temp  # put it in the slot
                c[i][w] = champ
    for i in range(1, n):
        if c[i][W-1] != 0:
            K.append(I[i])
    return c[n - 1][W - 1], K


print "Maximum knapsack value, and items:", knapsackContents(I, W)
