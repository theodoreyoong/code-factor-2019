def getFactors(k):
    factors = []
    for i in range(1, int(math.floor(math.sqrt(k))) + 1):
        if k%i == 0:
            factors.extend([i, k//i])
    return (sorted(factors, reverse = true))

# Preferences imply use of priority queue

def maxParticipants(n, prefNums):
    factorsList = [getFactors(e) for e in prefNums]
    pq = []
    for factors in factorsList:
        heappq.heappush(pq, (len(factors), factors))
    chosenCars = set()
    while pq:
        current = heappq.heappop(pq)[1]
        for factor in current:
            if factor <= n and factor not in chosenCars:
                chosenCars.add(factor)
                break
    return len(chosenCars)
