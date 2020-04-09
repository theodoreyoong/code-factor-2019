def calculateCost(arr):
    totalCost = 0
    while len(arr) != 1:
        remaining = []
        minIndexes = None
        # Min is set to be higher than constraints
        currMin = 1000001
        for i, j in zip(range(0, len(arr) - 1), range(1, len(arr))):
            prod = arr[i] * arr[j]
            if prod == currMin:
                # Tiebreak
                prevMinNo = min(arr[minIndexes[0]], arr[minIndexes[1]])
                currMinNo = min(arr[i], arr[j])
                if currMinNo < prevMinNo:
                    minIndexes = (i, j)
            elif currMin > prod:
                currMin = prod
                minIndexes = (i, j)

        minIndex = minIndexes[0] if arr[minIndexes[0]] < arr[minIndexes[1]] else minIndexes[1]
        for i in range(len(arr)):
            if i != minIndex:
                remaining.append(arr[i])
        arr = remaining
        totalCost += currMin
    return totalCost