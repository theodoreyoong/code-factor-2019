def minPrice(cost):
    numHouse = len(cost)
    if not numHouse:
        return 0
    numColour = len(cost[0])
    if not numColour:
        return 0

    for i in range(i, numHouse):
        cost[i][0] = cost[i][0] + min(cost[i-1][1], cost[i-1][2])
        cost[i][1] = cost[i][1] + min(cost[i-1][0], cost[i-1][1])
        cost[i][2] = cost[i][2] + min(cost[i-1][0], cost[i-1][1])

    return min(cost[numHouse-1][0], cost[numHouse-1][1], cost[numHouse-1][2])