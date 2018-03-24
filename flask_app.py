
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
import random as r

app = Flask(__name__)

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

def printStats(arr):
    return "STR " + str(arr[0]) + "\nDEX " + str(arr[1]) + "\nCON " + str(arr[2]) + "\nINT " + str(arr[3]) + "\nWIS " + str(arr[4]) + "\nCHA " + str(arr[5])

def isNonVariantHuman(arr):
    oddCount = 0
    for stat in arr:
        if stat%2 == 0:
            oddCount += 1
    return oddCount > 3

def humanCheck(sortArr):
    return r.randint(0, 2) == 3 and sortArr[0] %2 == 1 and sortArr[0] %2 == 1

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

def shuffleHighest(sortArr):
    return sortArr[1:] + sortArr[:1]

def strDex(arr, sortArr):
    arr[0] = arr[0] + 2
    arr[1] = arr[1] + 1
    return "Bugbear"
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
        if r.randint(0, 1) == 1:
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
    sortArr = shuffleHighest(sortArr)
    return pickRaceByStats(arr, sortArr, highestStatIndexes)
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
    if r.randint(0, 10) == 10 and arr[5] %2 == 0:
        arr[0] = arr[0] + 1
        arr[5] = arr[5] + 2
        arr[sortArr[2]] = arr[sortArr[2]] + 1
        return "Half-Elf"
    if sortArr[2] == 2 and arr[0] % 2 == 1 and arr[2] % 2 == 1 and arr[5] % 2 == 1:
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
    if r.randint(0, 3) == 3 and sortArr[5] == 0:
        arr[0] = arr[0] - 2
        arr[1] = arr[1] + 2
        return "Kobold"
    elif arr[2] % 2 != 0:
        if r.randint(0, 1) == 1:
            arr[1] = arr[1] + 2
            arr[2] = arr[2] + 1
            return "Stout Halfling"
        else:
            arr[1] = arr[1] + 2
            arr[2] = arr[2] + 1
            return "Goblin"
    else:
        arr[1] = arr[1] + 1
        arr[2] = arr[2] + 2
        return "Air Genasi"
def dexInt(arr, sortArr):
    if r.randint(0, 3) == 3 and sortArr[5] == 0:
        arr[0] = arr[0] - 2
        arr[1] = arr[1] + 2
        return "Kobold"
    elif arr[1] % 2 != 0:
        if r.randint(0, 1) == 1:
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
    if r.randint(0, 3) == 3 and sortArr[5] == 0:
        arr[0] = arr[0] - 2
        arr[1] = arr[1] + 2
        return "Kobold"
    rand = r.randint(0, 3)
    if rand == 3:
        arr[1] = arr[1] + 2
        arr[4] = arr[4] + 1
        return "Kenku"
    elif rand == 2:
        arr[1] = arr[1] + 2
        arr[4] = arr[4] + 1
        return "Ghostwise Halfling"
    else:
        arr[1] = arr[1] + 2
        arr[4] = arr[4] + 1
        return "Wood Elf"
def dexCha(arr, sortArr):
    if r.randint(0, 10) == 10 and arr[5] %2 == 0:
        arr[1] = arr[1] + 1
        arr[5] = arr[5] + 2
        arr[sortArr[2]] = arr[sortArr[2]] + 1
        return "Half-Elf"
    if r.randint(0, 3) == 3 and sortArr[5] == 0:
        arr[0] = arr[0] - 2
        arr[1] = arr[1] + 2
        return "Kobold"
    rand = r.randint(0, 3)
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
    if r.randint(0, 10) == 10 and arr[5] %2 == 0:
        arr[2] = arr[2] + 1
        arr[5] = arr[5] + 2
        arr[sortArr[2]] = arr[sortArr[2]] + 1
        return "Half-Elf"
    if sortArr[2] == 2 and arr[0] % 2 == 1 and arr[2] % 2 == 1 and arr[5] % 2 == 1:
        arr[0] = arr[0] + 1
        arr[1] = arr[1] + 1
        arr[5] = arr[5] + 1
        return "Triton"
    else:
        arr[2] = arr[2] + 1
        arr[5] = arr[5] + 2
        return "Scourge Aasimar"
def intWis(arr, sortArr):
    sortArr = shuffleHighest(sortArr)
    return pickRaceByStats(arr, sortArr, highestStatIndexes)
def intCha(arr, sortArr):
    if r.randint(0, 10) == 10 and arr[5] %2 == 0:
        arr[3] = arr[3] + 1
        arr[5] = arr[5] + 2
        arr[sortArr[2]] = arr[sortArr[2]] + 1
        return "Half-Elf"
    if r.randint(0, 3) == 3:
        arr[3] = arr[3] + 1
        arr[5] = arr[5] + 2
        return "Yuan-Ti Pureblood"
    else:
        arr[3] = arr[3] + 1
        arr[5] = arr[5] + 2
        return "Tiefling"
def wisCha(arr, sortArr):
    if r.randint(0, 10) == 10 and arr[5] %2 == 0:
        arr[4] = arr[4] + 1
        arr[5] = arr[5] + 2
        arr[sortArr[2]] = arr[sortArr[2]] + 1
        return "Half-Elf"
    arr[4] = arr[4] + 1
    arr[5] = arr[5] + 2
    return "Protector Aasimar"

@app.route('/')
def fullRoll():
    arr = rollStats()
    raceStr = pickRaceByStats(arr, rankStats(arr), highestStatIndexes)
    return render_template('fullRoll.html', race=raceStr, statStr=arr[0], statDex=arr[1], statCon=arr[2], statInt=arr[3], statWis=arr[4], statCha=arr[5])

@app.route('/stats')
def justStats():
    arr = rollStats()
    return render_template('justStats.html', statStr=arr[0], statDex=arr[1], statCon=arr[2], statInt=arr[3], statWis=arr[4], statCha=arr[5])