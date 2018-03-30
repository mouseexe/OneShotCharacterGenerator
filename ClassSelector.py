import Util as u

def pickClassByStats(arr, sortArr, checkStat):
    if sortArr[checkStat] == 0: #High Strength
        if arr[5] > 13:
            return "Paladin"
        elif u.d(2) == 2:
            return "Fighter"
        else:
            return "Barbarian"
    elif sortArr[checkStat] == 1: #High Dexterity
        if arr[4] > 13:
            if u.d(1) == 1:
                return "Ranger"
            else:
                return "Monk"
        elif u.d(2) == 2:
            return "Fighter"
        else:
            return "Rogue"
    elif sortArr[checkStat] == 2: #High Constitution
        return pickClassByStats(arr, sortArr, checkStat+1)
    elif sortArr[checkStat] == 3: #High Intelligence
        if u.d(1) == 1:
            return "Wizard"
        else:
            return "Artificer"
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