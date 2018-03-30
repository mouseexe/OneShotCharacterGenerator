import Util as u

def pickClassByStats(arr, sortArr, checkStat):
    if sortArr[checkStat] == 0: #High Strength
        if arr[5] > 13:
            return paladin(arr, sortArr)
        elif u.d(2) == 2:
            return fighter(arr, sortArr)
        else:
            return barbarian(arr, sortArr)
    elif sortArr[checkStat] == 1: #High Dexterity
        if arr[4] > 13:
            if u.d(1) == 1:
                return ranger(arr, sortArr)
            else:
                return monk(arr, sortArr)
        elif u.d(2) == 2:
            return fighter(arr, sortArr)
        else:
            return rogue(arr, sortArr)
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
                return ranger(arr, sortArr)
            else:
                return monk(arr, sortArr)
        elif u.d(1) == 1:
            return druid(arr, sortArr)
        else:
            return cleric(arr, sortArr)
    elif sortArr[checkStat] == 5: #High Charisma
        rand = u.d(2)
        if arr[0] > 15:
            return paladin(arr, sortArr)
        elif rand == 2:
            return bard(arr, sortArr)
        elif rand == 1:
            return sorcerer(arr, sortArr)
        else:
            return warlock(arr, sortArr)

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

def bard(arr, sortArr):
    rand = u.d(4)
    if rand == 4 and arr[1] > 13:
        return "Bard (College of Valor)"
    elif rand == 3 and arr[1] > 13:
        return "Bard (College of Swords)"
    elif rand == 2:
        return "Bard (College of Glamour)"
    elif rand == 1:
        return "Bard (College of Whispers)"
    else:
        return "Bard (College of Lore)"

def cleric(arr, sortArr):
    rand = u.d(9)
    if rand == 9:
        return "Cleric (Grave Domain)"
    elif rand == 8:
        return "Cleric (Forge Domain)"
    elif rand == 7:
        return "Cleric (Divine Domain)"
    elif rand == 6:
        return "Cleric (War Domain)"
    elif rand == 5:
        return "Cleric (Light Domain)"
    elif rand == 4:
        return "Cleric (Nature Domain)"
    elif rand == 3:
        return "Cleric (Trickery Domain)"
    elif rand == 2:
        return "Cleric (Tempest Domain)"
    elif rand == 1:
        return "Cleric (Knowledge Domain)"
    else:
        return "Cleric (Life Domain)"

def druid(arr, sortArr):
    rand = u.d(3)
    if rand == 3:
        return "Druid (Circle of Dreams)"
    elif rand == 2:
        return "Druid (Circle of the Shepherd)"
    elif rand == 1:
        return "Druid (Circle of the Land)"
    else:
        return "Druid (Circle of the Moon)"

def monk(arr, sortArr):
    rand = u.d(6)
    if rand == 6:
        return "Monk (Way of the Open Hand)"
    elif rand == 5:
        return "Monk (Way of the Long Death)"
    elif rand == 4:
        return "Monk (Way of the Sun Soul)"
    elif rand == 3:
        return "Monk (Way of the Kensei)"
    elif rand == 2:
        return "Monk (Way of the Drunken Master)"
    elif rand == 1:
        return "Monk (Way of Shadow)"
    else:
        return "Monk (Way of the Four Elements)"

def paladin(arr, sortArr):
    rand = u.d(5)
    if rand == 5:
        return "Paladin (Oath of Conquest)"
    elif rand == 4:
        return "Paladin (Oath of Redemption)"
    elif rand == 3:
        return "Paladin (Oath of the Crown)"
    elif rand == 2:
        return "Paladin (Oath of the Ancients)"
    elif rand == 1:
        return "Paladin (Oath of Vengeance)"
    else:
        return "Paladin (Oath of Devotion)"

def ranger(arr, sortArr):
    rand = u.d(4)
    if rand == 4:
        return "Ranger (Hunter)"
    elif rand == 3:
        return "Ranger (Beast Master)"
    elif rand == 2:
        return "Ranger (Gloom Stalker)"
    elif rand == 1:
        return "Ranger (Monster Slayer)"
    else:
        return "Ranger (Horizon Walker)"

def rogue(arr, sortArr):
    rand = u.d(6)
    if rand == 6 and arr[3] > 13:
        return "Rogue (Arcane Trickster)"
    elif rand == 5:
        return "Rogue (Scout)"
    elif rand == 4:
        return "Rogue (Inquisitive)"
    elif rand == 3:
        return "Rogue (Swashbuckler)"
    elif rand == 2:
        return "Rogue (Mastermind)"
    elif rand == 1:
        return "Rogue (Thief)"
    else:
        return "Rogue (Assassin)"

def sorcerer(arr, sortArr):
    rand = u.d(4)
    if rand == 4:
        return "Sorcerer (Draconic Bloodline)"
    elif rand == 3:
        return "Sorcerer (Wild Magic)"
    elif rand == 2:
        return "Sorcerer (Shadow Magic)"
    elif rand == 1:
        return "Sorcerer (Storm Sorcery)"
    else:
        return "Sorcerer (Divine Soul)"

def warlock(arr, sortArr):
    rand = u.d(2)
    if rand == 2:
        boon = "Pact of the Tome)"
    elif rand == 1:
        boon = "Pact of the Chain)"
    else:
        boon = "Pact of the Blade)"
    rand = u.d(5)
    if rand == 5:
        return "Warlock (The Hexblade," + boon
    elif rand == 4:
        return "Warlock (The Celestial," + boon
    elif rand == 3:
        return "Warlock (The Undying," + boon
    elif rand == 2:
        return "Warlock (The Fiend," + boon
    elif rand == 1:
        return "Warlock (The Archfey," + boon
    else:
        return "Warlock (The Great Old One," + boon
