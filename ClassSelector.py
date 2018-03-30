import Util as u

def pickClassByStats(arr, sortArr, checkStat):
    if sortArr[checkStat] == 0: #High Strength
        if arr[5] > 13:
            return "Paladin"
        elif u.d(2) == 2:
            return fighter(arr, sortArr)
        else:
            return barbarian(arr, sortArr)
    elif sortArr[checkStat] == 1: #High Dexterity
        if arr[4] > 13:
            if u.d(1) == 1:
                return "Ranger"
            else:
                return "Monk"
        elif u.d(2) == 2:
            return fighter(arr, sortArr)
        else:
            return "Rogue"
    elif sortArr[checkStat] == 2: #High Constitution
        return pickClassByStats(arr, sortArr, checkStat+1)
    elif sortArr[checkStat] == 3: #High Intelligence
        if u.d(1) == 1:
            return wizard(arr, sortArr)
        else:
            return artificer(arr, sortArr)
    elif sortArr[checkStat] == 4: #High Wisdom
        if arr[1] > 15:
            if u.d(1) == 1:
                return "Ranger"
            else:
                return "Monk"
        elif u.d(1) == 1:
            return "Druid"
        else:
            return "Cleric"
    elif sortArr[checkStat] == 5: #High Charisma
        rand = u.d(2)
        if arr[0] > 15:
            return "Paladin"
        elif rand == 2:
            return "Bard"
        elif rand == 1:
            return "Sorcerer"
        else:
            return "Warlock"

def wizard(arr, sortArr):
    rand = u.d(9)
    if rand == 9 and arr[1] > 13:
        return "Wizard (Bladesinger)"
    elif rand == 8:
        return "Wizard (War Magic)"
    elif rand == 7:
        return "Wizard (School of Abjuration)"
    elif rand == 6:
        return "Wizard (School of Conjuration)"
    elif rand == 5:
        return "Wizard (School of Divination)"
    elif rand == 4:
        return "Wizard (School of Enchantment)"
    elif rand == 3:
        return "Wizard (School of Evocation)"
    elif rand == 2:
        return "Wizard (School of Illusion)"
    elif rand == 1:
        return "Wizard (School of Necromancy)"
    else:
        return "Wizard (School of Transmutation)"

def artificer(arr, sortArr):
    if u.d(1) == 1 and arr[1] > 13:
        return "Artificer (Gunsmith)"
    else:
        return "Artificer (Alchemist)"

def fighter(arr, sortArr):
    rand = u.d(6)
    if rand == 6 and arr[3] > 13:
        return "Fighter (Eldritch Knight)"
    elif rand == 5:
        return "Fighter (Purple Dragon Knight)"
    elif rand == 4 and arr[1] > 15:
        return "Fighter (Arcane Archer)"
    elif rand == 3:
        return "Fighter (Samurai)"
    elif rand == 2:
        return "Fighter (Cavalier)"
    elif rand == 1:
        return "Fighter (Battle Master)"
    else:
        return "Fighter (Champion)"

def barbarian(arr, sortArr):
    rand = u.d(5)
    if rand == 5:
        return "Barbarian (Path of the Berserker)"
    elif rand == 4:
        return "Barbarian (Path of the Totem Warrior)"
    elif rand == 3:
        return "Barbarian (Path of the Ancestral Guardian)"
    elif rand == 2:
        return "Barbarian (Path of the Storm Herald)"
    elif rand == 1:
        return "Barbarian (Path of the Zealot)"
    else:
        return "Barbarian (Path of the Battlerager)"