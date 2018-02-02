import random as r

#TODO smarter race selection

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

def highestStatIndexes(arr):
    firstIdx = 0
    for idx in range(len(arr)):
        if arr[idx] > arr[firstIdx]:
            firstIdx = idx
    secondIdx = 5-firstIdx
    for idx in range(len(arr)):
        if arr[idx] > arr[secondIdx] and idx != firstIdx:
            secondIdx = idx
    return (firstIdx, secondIdx)

def noGoodRaceStatIndexes(arr):
    firstIdx = 0
    for idx in range(len(arr)):
        if arr[idx] > arr[firstIdx]:
            firstIdx = idx
    secondIdx = 5-firstIdx
    for idx in range(len(arr)):
        if arr[idx] > arr[secondIdx] and idx != firstIdx:
            secondIdx = idx
    thirdIdx = 5 - firstIdx
    for idx in range(len(arr)):
        if arr[idx] > arr[thirdIdx] and idx != firstIdx and idx != secondIdx:
            thirdIdx = idx
    return (firstIdx, thirdIdx)

def pickRaceByStats(arr, statPicker):
    classes = {
        (0, 1): strDex,
        (1, 0): strDex,
        (0, 2): strCon,
        (2, 0): strCon,
        (0, 3): strInt,
        (3, 0): strInt,
        (0, 4): strWis,
        (4, 0): strWis,
        (0, 5): strCha,
        (5, 0): strCha,
        (1, 2): dexCon,
        (2, 1): dexCon,
        (1, 3): dexInt,
        (3, 1): dexInt,
        (1, 4): dexWis,
        (4, 1): dexWis,
        (1, 5): dexCha,
        (5, 1): dexCha,
        (2, 3): conInt,
        (3, 2): conInt,
        (2, 4): conWis,
        (4, 2): conWis,
        (2, 5): conCha,
        (5, 2): conCha,
        (3, 4): intWis,
        (4, 3): intWis,
        (3, 5): intCha,
        (5, 3): intCha,
        (4, 5): wisCha,
        (5, 4): wisCha
    }
    func = classes.get(statPicker(arr), lambda: "stat error")
    return func(arr)

def printStats(arr):
    return "STR " + str(arr[0]) + "\nDEX " + str(arr[1]) + "\nCON " + str(arr[2]) + "\nINT " + str(arr[3]) + "\nWIS " + str(arr[4]) + "\nCHA " + str(arr[5])

def isNonVariantHuman(arr):
    oddCount = 0
    for stat in arr:
        if stat%2 == 0:
            oddCount +=1
    return oddCount > 3

def strDex(arr):
    return pickRaceByStats(arr, noGoodRaceStatIndexes)
def strCon(arr):
    if arr[2]%2 != 0:
        arr[0] = arr[0]+2
        arr[2] = arr[2]+1
        return "Half-Orc"
    else:
        arr[0] = arr[0] + 2
        arr[2] = arr[2] + 2
        return "Mountain Dwarf"
def strInt(arr):
    if arr[0]%2 != 0 and arr[3]%2 != 0 and isNonVariantHuman(arr):
        arr[0] = arr[0] + 1
        arr[1] = arr[1] + 1
        arr[2] = arr[2] + 1
        arr[3] = arr[3] + 1
        arr[4] = arr[4] + 1
        arr[5] = arr[5] + 1
        return "Human"
    else:
        arr[0] = arr[0] + 1
        arr[3] = arr[3] + 1
        return "Variant Human"
def strWis(arr):
    if arr[0]%2 != 0 and arr[4]%2 != 0 and isNonVariantHuman(arr):
        arr[0] = arr[0] + 1
        arr[1] = arr[1] + 1
        arr[2] = arr[2] + 1
        arr[3] = arr[3] + 1
        arr[4] = arr[4] + 1
        arr[5] = arr[5] + 1
        return "Human"
    else:
        arr[0] = arr[0] + 1
        arr[4] = arr[4] + 1
        return "Variant Human"
def strCha(arr):
    if arr[5]%2 != 0:
        arr[0] = arr[0] + 2
        arr[5] = arr[5] + 1
        return "Dragonborn"
    else:
        arr[0] = arr[0] + 1
        arr[5] = arr[5] + 2
        return "Half-Elf"
def dexCon(arr):
    arr[1] = arr[1] + 2
    arr[2] = arr[2] + 1
    return "Stout Halfling"
def dexInt(arr):
    if arr[1] % 2 != 0:
        arr[1] = arr[1] + 1
        arr[3] = arr[3] + 2
        return "Forest Gnome"
    else:
        arr[1] = arr[1] + 2
        arr[3] = arr[3] + 1
        return "High Elf"
def dexWis(arr):
    arr[1] = arr[1] + 2
    arr[4] = arr[4] + 1
    return "Wood Elf"
def dexCha(arr):
    if r.randint(0,1) == 1:
        arr[1] = arr[1] + 2
        arr[5] = arr[5] + 1
        return "Drow"
    else:
        arr[1] = arr[1] + 2
        arr[5] = arr[5] + 1
        return "Lightfoot Halfling"
def conInt(arr):
    arr[2] = arr[2] + 1
    arr[3] = arr[3] + 2
    return "Rock Gnome"
def conWis(arr):
    arr[2] = arr[2] + 1
    arr[4] = arr[4] + 2
    return "Hill Dwarf"
def conCha(arr):
    arr[2] = arr[2] + 1
    arr[5] = arr[5] + 2
    return "Half-Elf"
def intWis(arr):
    return pickRaceByStats(arr, noGoodRaceStatIndexes)
def intCha(arr):
    arr[3] = arr[3] + 1
    arr[5] = arr[5] + 2
    return "Tiefling"
def wisCha(arr):
    arr[4] = arr[4] + 1
    arr[5] = arr[5] + 2
    return "Half-Elf"

def main():
    arr = rollStats()
    #arr = [13, 12, 14, 18, 16, 14]
    race = pickRaceByStats(arr, highestStatIndexes)
    print(race + "\n" + printStats(arr))

main()