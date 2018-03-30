import Util as u

def pickRaceByStats(arr, sortArr, statPicker):
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
    func = classes.get(statPicker(sortArr), lambda: "stat error")
    if humanCheck(sortArr):
        return buildHuman(arr, sortArr)
    else:
        return func(arr, sortArr)

def isNonVariantHuman(arr):
    oddCount = 0
    for stat in arr:
        if stat%2 == 0:
            oddCount += 1
    return oddCount > 3

def humanCheck(sortArr):
    return u.d(2) == 2 and sortArr[0] %2 == 1 and sortArr[0] %2 == 1

def buildHuman(arr, sortArr):
    if isNonVariantHuman(arr):
        arr[0] = arr[0] + 1
        arr[1] = arr[1] + 1
        arr[2] = arr[2] + 1
        arr[3] = arr[3] + 1
        arr[4] = arr[4] + 1
        arr[5] = arr[5] + 1
        return "Human"
    else:
        arr[sortArr[0]] = arr[sortArr[0]] + 1
        arr[sortArr[1]] = arr[sortArr[1]] + 1
        return "Variant Human"

def strDex(arr, sortArr):
    if u.d(2) == 2:
        arr[0] = arr[0] + 2
        arr[1] = arr[1] + 1
        return "Bugbear"
    else:
        sortArr = u.shuffleHighest(sortArr)
        return pickRaceByStats(arr, sortArr, u.highestStatIndexes)
def strCon(arr, sortArr):
    if sortArr[2] == 5 and arr[0] %2 == 1 and arr[2] %2 == 1 and arr[5] %2 == 1:
        arr[0] = arr[0] + 1
        arr[2] = arr[2] + 1
        arr[5] = arr[5] + 1
        return "Triton"
    elif arr[2]%2 != 0:
        if sortArr[5] == 3:
            arr[0] = arr[0] + 2
            arr[2] = arr[2] + 1
            arr[3] = arr[3] - 2
            return "Orc"
        if r.randint(0, 1) == 1:
            arr[0] = arr[0] + 2
            arr[2] = arr[2] + 1
            return "Half-Orc"
        else:
            arr[0] = arr[0] + 2
            arr[2] = arr[2] + 1
            return "Goliath"
    elif arr[1]%2 != 0:
        if u.d(1) == 1:
            arr[0] = arr[0] + 1
            arr[2] = arr[2] + 2
            return "Duergar Dwarf"
        else:
            arr[0] = arr[0] + 1
            arr[2] = arr[2] + 2
            return "Earth Genasi"
    else:
        arr[0] = arr[0] + 2
        arr[2] = arr[2] + 2
        return "Mountain Dwarf"
def strInt(arr, sortArr):
    sortArr = u.shuffleHighest(sortArr)
    return pickRaceByStats(arr, sortArr, u.highestStatIndexes)
def strWis(arr, sortArr):
    if arr[0] % 2 != 0:
        arr[0] = arr[0] + 1
        arr[4] = arr[4] + 2
        return "Firbolg"
    else:
        arr[0] = arr[0] + 2
        arr[4] = arr[4] + 1
        return "Tortle"
def strCha(arr, sortArr):
    if u.d(5) == 5 and arr[5] %2 == 0:
        arr[0] = arr[0] + 1
        arr[5] = arr[5] + 2
        arr[sortArr[2]] = arr[sortArr[2]] + 1
        return "Half-Elf"
    elif sortArr[2] == 2 and arr[0] % 2 == 1 and arr[2] % 2 == 1 and arr[5] % 2 == 1:
        arr[0] = arr[0] + 1
        arr[1] = arr[1] + 1
        arr[5] = arr[5] + 1
        return "Triton"
    elif arr[5]%2 != 0:
        arr[0] = arr[0] + 2
        arr[5] = arr[5] + 1
        return "Dragonborn"
    else:
        arr[0] = arr[0] + 1
        arr[5] = arr[5] + 2
        return "Fallen Aasimar"
def dexCon(arr, sortArr):
    if u.d(3) == 3 and sortArr[5] == 0:
        arr[0] = arr[0] - 2
        arr[1] = arr[1] + 2
        return "Kobold"
    elif arr[2] % 2 != 0:
        if u.d(2) == 2:
            arr[1] = arr[1] + 2
            arr[2] = arr[2] + 1
            return "Goblin"
        else:
            arr[1] = arr[1] + 2
            arr[2] = arr[2] + 1
            return "Stout Halfling"
    else:
        arr[1] = arr[1] + 1
        arr[2] = arr[2] + 2
        return "Air Genasi"
def dexInt(arr, sortArr):
    if u.d(3) == 3 and sortArr[5] == 0:
        arr[0] = arr[0] - 2
        arr[1] = arr[1] + 2
        return "Kobold"
    elif arr[1] % 2 != 0:
        if u.d(1) == 1:
            arr[1] = arr[1] + 1
            arr[3] = arr[3] + 2
            return "Forest Gnome"
        else:
            arr[1] = arr[1] + 1
            arr[3] = arr[3] + 2
            return "Deep Gnome"
    else:
        arr[1] = arr[1] + 2
        arr[3] = arr[3] + 1
        return "High Elf"
def dexWis(arr, sortArr):
    if u.d(3) == 3 and sortArr[5] == 0:
        arr[0] = arr[0] - 2
        arr[1] = arr[1] + 2
        return "Kobold"
    rand = u.d(4)
    if rand == 4:
        arr[1] = arr[1] + 2
        arr[4] = arr[4] + 1
        return "Kenku"
    elif rand == 3:
        arr[1] = arr[1] + 2
        arr[4] = arr[4] + 1
        return "Ghostwise Halfling"
    else:
        arr[1] = arr[1] + 2
        arr[4] = arr[4] + 1
        return "Wood Elf"
def dexCha(arr, sortArr):
    if u.d(5) == 5 and arr[5] %2 == 0:
        arr[1] = arr[1] + 1
        arr[5] = arr[5] + 2
        arr[sortArr[2]] = arr[sortArr[2]] + 1
        return "Half-Elf"
    if u.d(3) == 3 and sortArr[5] == 0:
        arr[0] = arr[0] - 2
        arr[1] = arr[1] + 2
        return "Kobold"
    rand = u.d(3)
    if rand == 3:
        arr[1] = arr[1] + 2
        arr[5] = arr[5] + 1
        return "Drow"
    elif rand == 2:
        arr[1] = arr[1] + 2
        arr[5] = arr[5] + 1
        return "Tabaxi"
    else:
        arr[1] = arr[1] + 2
        arr[5] = arr[5] + 1
        return "Lightfoot Halfling"
def conInt(arr, sortArr):
    if arr[2] % 2 != 0:
        arr[2] = arr[2] + 1
        arr[3] = arr[3] + 2
        return "Rock Gnome"
    else:
        if r.randint(0, 1) == 1:
            arr[2] = arr[2] + 2
            arr[3] = arr[3] + 1
            return "Fire Genasi"
        else:
            arr[2] = arr[2] + 2
            arr[3] = arr[3] + 1
            return "Hobgoblin"
def conWis(arr, sortArr):
    if arr[2] % 2 != 0:
        arr[2] = arr[2] + 1
        arr[4] = arr[4] + 2
        return "Hill Dwarf"
    else:
        if r.randint(0, 1) == 1:
            arr[2] = arr[2] + 2
            arr[4] = arr[4] + 1
            return "Water Genasi"
        else:
            arr[2] = arr[2] + 2
            arr[4] = arr[4] + 1
            return "Lizardfolk"
def conCha(arr, sortArr):
    if u.d(1) == 1 and arr[5] %2 == 0:
        arr[2] = arr[2] + 1
        arr[5] = arr[5] + 2
        arr[sortArr[2]] = arr[sortArr[2]] + 1
        return "Half-Elf"
    elif sortArr[2] == 2 and arr[0] % 2 == 1 and arr[2] % 2 == 1 and arr[5] % 2 == 1:
        arr[0] = arr[0] + 1
        arr[1] = arr[1] + 1
        arr[5] = arr[5] + 1
        return "Triton"
    else:
        arr[2] = arr[2] + 1
        arr[5] = arr[5] + 2
        return "Scourge Aasimar"
def intWis(arr, sortArr):
    sortArr = u.shuffleHighest(sortArr)
    return pickRaceByStats(arr, sortArr, u.highestStatIndexes)
def intCha(arr, sortArr):
    if u.d(5) == 5 and arr[5] %2 == 0:
        arr[3] = arr[3] + 1
        arr[5] = arr[5] + 2
        arr[sortArr[2]] = arr[sortArr[2]] + 1
        return "Half-Elf"
    elif u.d(2) == 2:
        arr[3] = arr[3] + 1
        arr[5] = arr[5] + 2
        return "Yuan-Ti Pureblood"
    else:
        arr[3] = arr[3] + 1
        arr[5] = arr[5] + 2
        return "Tiefling"
def wisCha(arr, sortArr):
    if u.d(1) == 1 and arr[5] %2 == 0:
        arr[4] = arr[4] + 1
        arr[5] = arr[5] + 2
        arr[sortArr[2]] = arr[sortArr[2]] + 1
        return "Half-Elf"
    else:
        arr[4] = arr[4] + 1
        arr[5] = arr[5] + 2
        return "Protector Aasimar"