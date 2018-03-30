import random as r

def rollStats():
    statsArr = [rollOneStat(), rollOneStat(), rollOneStat(), rollOneStat(), rollOneStat(), rollOneStat()]
    overFifteen = 0
    for stat in statsArr:
        if stat >= 15:
            overFifteen += 1
    if overFifteen >= 2:
        return statsArr
    else:
        return rollStats()

def rollOneStat():
    arr = [r.randint(1, 6), r.randint(1, 6), r.randint(1, 6), r.randint(1, 6)]
    return dropLowest(arr)

def dropLowest(arr):
    minIdx = 0
    for idx in range(len(arr)):
        if arr[idx] < arr[minIdx]:
            minIdx = idx
    total = 0
    for idx in range(len(arr)):
        if idx != minIdx:
            total += arr[idx]
    return total

def highestStatIndexes(sortArr):
    return (sortArr[0], sortArr[1])

def rankStats(arr):
    highToLow = arr[:]
    highToLow = sorted(range(len(highToLow)), key=lambda k: highToLow[k])
    highToLow.reverse()
    return highToLow

def shuffleHighest(sortArr):
    return sortArr[0:1] + sortArr[2:] + sortArr[1:2]

def d(sides):
    return r.randint(0, sides) #TODO refactor