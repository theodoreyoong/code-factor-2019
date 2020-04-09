def getMinimumMoves(identification):
    # Start at the front.
    l = len(identification)
    s = sorted(identification)
    k = 0
    expectedItem = s[0]
    currMoves = l
    for i in range(l):
        if identification[i] == expectedItem:
            if k < l-1:
                k += 1
                expectedItem = s[k]
            currMoves -= 1
    return currMoves