#Narrative: Determines the Type of the move and sends the opponent's type
#to the appropriate function
def identifyType1(type1, type2):
    if type1 == "Normal":
        damage = normalType(type2)
    elif type1 == "Fire":
        damage = fireType(type2)
    elif type1 == "Water":
        damage = waterType(type2)
    elif type1 == "Grass":
        damage = grassType(type2)
    elif type1 == "Electric":
        damage = electricType(type2)
    elif type1 == "Ice":
        damage = iceType(type2)
    elif type1 == "Fighting":
        damage = fightingType(type2)
    elif type1 == "Poison":
        damage = poisonType(type2)
    elif type1 == "Ground":
        damage = groundType(type2)
    elif type1 == "Flying":
        damage = flyingType(type2)
    elif type1 == "Psychic":
        damage = psychicType(type2)
    elif type1 == "Bug":
        damage = bugType(type2)
    elif type1 == "Rock":
        damage = rockType(type2)
    elif type1 == "Ghost":
        damage = ghostType(type2)
    elif type1 == "Dragon":
        damage = dragonType(type2)
    elif type1 == "Dark":
        damage = darkType(type2)
    elif type1 == "Steel":
        damage = steelType(type2)
    elif type1 == "Fairy":
        damage = fairyType(type2)
    else:
        print("Error")
    return damage
#Returns the effectiveness between the two types


#Narrative: Determines how the Normal Type Matches up with the other types, and returns
#the effectiveness
def normalType(type2):
    if type2 == "Normal":
        damage = 1
        return damage
    elif type2 == "Fire":
        damage = 1
        return damage
    elif type2 == "Water":
        damage = 1
        return damage
    elif type2 == "Grass":
        damage = 1
        return damage
    elif type2 == "Electric":
        damage = 1
        return damage
    elif type2 == "Ice":
        damage = 1
        return damage
    elif type2 == "Fighting":
        damage = 1
        return damage
    elif type2 == "Poison":
        damage = 1
        return damage
    elif type2 == "Ground":
        damage = 1
        return damage
    elif type2 == "Flying":
        damage = 1
        return damage
    elif type2 == "Psychic":
        damage = 1
        return damage
    elif type2 == "Bug":
        damage = 1
        return damage
    elif type2 == "Rock":
        damage = .5
        return damage
    elif type2 == "Ghost":
        damage = 0
        return damage
    elif type2 == "Dragon":
        damage = 1
        return damage
    elif type2 == "Dark":
        damage = 1
        return damage
    elif type2 == "Steel":
        damage = .5
        return damage
    elif type2 == "Fairy":
        damage = 1
        return damage
    else:
        print("Error")

#Narrative: Determines how the Fire Type Matches up with the other types, and returns
#the effectiveness
def fireType(type2):
    if type2 == "Normal":
        damage = 1
        return damage
    elif type2 == "Fire":
        damage = .5
        return damage
    elif type2 == "Water":
        damage = .5
        return damage
    elif type2 == "Grass":
        damage = 2
        return damage
    elif type2 == "Electric":
        damage = 1
        return damage
    elif type2 == "Ice":
        damage = 2
        return damage
    elif type2 == "Fighting":
        damage = 1
        return damage
    elif type2 == "Poison":
        damage = 1
        return damage
    elif type2 == "Ground":
        damage = 1
        return damage
    elif type2 == "Flying":
        damage = 1
        return damage
    elif type2 == "Psychic":
        damage = 1
        return damage
    elif type2 == "Bug":
        damage = 2
        return damage
    elif type2 == "Rock":
        damage = .5
        return damage
    elif type2 == "Ghost":
        damage = 1
        return damage
    elif type2 == "Dragon":
        damage = .5
        return damage
    elif type2 == "Dark":
        damage = 1
        return damage
    elif type2 == "Steel":
        damage = 2
        return damage
    elif type2 == "Fairy":
        damage = 1
        return damage
    else:
        print("Error")

#Narrative: Determines how the Water Type Matches up with the other types, and returns
#the effectiveness
def waterType(type2):
    if type2 == "Normal":
        damage = 1
        return damage
    elif type2 == "Fire":
        damage = 2
        return damage
    elif type2 == "Water":
        damage = .5
        return damage
    elif type2 == "Grass":
        damage = .5
        return damage
    elif type2 == "Electric":
        damage = 1
        return damage
    elif type2 == "Ice":
        damage = 1
        return damage
    elif type2 == "Fighting":
        damage = 1
        return damage
    elif type2 == "Poison":
        damage = 1
        return damage
    elif type2 == "Ground":
        damage = 2
        return damage
    elif type2 == "Flying":
        damage = 1
        return damage
    elif type2 == "Psychic":
        damage = 1
        return damage
    elif type2 == "Bug":
        damage = 1
        return damage
    elif type2 == "Rock":
        damage = 2
        return damage
    elif type2 == "Ghost":
        damage = 1
        return damage
    elif type2 == "Dragon":
        damage = .5
        return damage
    elif type2 == "Dark":
        damage = 1
        return damage
    elif type2 == "Steel":
        damage = 1
        return damage
    elif type2 == "Fairy":
        damage = 1
        return damage
    else:
        print("Error")

#Narrative: Determines how the Grass Type Matches up with the other types, and returns
#the effectiveness
def grassType(type2):
    if type2 == "Normal":
        damage = 1
        return damage
    elif type2 == "Fire":
        damage = .5
        return damage
    elif type2 == "Water":
        damage = 2
        return damage
    elif type2 == "Grass":
        damage = .5
        return damage
    elif type2 == "Electric":
        damage = 1
        return damage
    elif type2 == "Ice":
        damage = 1
        return damage
    elif type2 == "Fighting":
        damage = 1
        return damage
    elif type2 == "Poison":
        damage = .5
        return damage
    elif type2 == "Ground":
        damage = 2
        return damage
    elif type2 == "Flying":
        damage = .5
        return damage
    elif type2 == "Psychic":
        damage = 1
        return damage
    elif type2 == "Bug":
        damage = .5
        return damage
    elif type2 == "Rock":
        damage = 2
        return damage
    elif type2 == "Ghost":
        damage = 1
        return damage
    elif type2 == "Dragon":
        damage = .5
        return damage
    elif type2 == "Dark":
        damage = 1
        return damage
    elif type2 == "Steel":
        damage = .5
        return damage
    elif type2 == "Fairy":
        damage = 1
        return damage
    else:
        print("Error")

#Narrative: Determines how the Electric Type Matches up with the other types, and returns
#the effectiveness
def electricType(type2):
    if type2 == "Normal":
        damage = 1
        return damage
    elif type2 == "Fire":
        damage = 1
        return damage
    elif type2 == "Water":
        damage = 2
        return damage
    elif type2 == "Grass":
        damage = .5
        return damage
    elif type2 == "Electric":
        damage = .5
        return damage
    elif type2 == "Ice":
        damage = 1
        return damage
    elif type2 == "Fighting":
        damage = 1
        return damage
    elif type2 == "Poison":
        damage = 1
        return damage
    elif type2 == "Ground":
        damage = 0
        return damage
    elif type2 == "Flying":
        damage = 2
        return damage
    elif type2 == "Psychic":
        damage = 1
        return damage
    elif type2 == "Bug":
        damage = 1
        return damage
    elif type2 == "Rock":
        damage = 1
        return damage
    elif type2 == "Ghost":
        damage = 1
        return damage
    elif type2 == "Dragon":
        damage = .5
        return damage
    elif type2 == "Dark":
        damage = 1
        return damage
    elif type2 == "Steel":
        damage = 1
        return damage
    elif type2 == "Fairy":
        damage = 1
        return damage
    else:
        print("Error")

#Narrative: Determines how the Ice Type Matches up with the other types, and returns
#the effectiveness
def iceType(type2):
    if type2 == "Normal":
        damage = 1
        return damage
    elif type2 == "Fire":
        damage = .5
        return damage
    elif type2 == "Water":
        damage = .5
        return damage
    elif type2 == "Grass":
        damage = 2
        return damage
    elif type2 == "Electric":
        damage = 1
        return damage
    elif type2 == "Ice":
        damage = .5
        return damage
    elif type2 == "Fighting":
        damage = 1
        return damage
    elif type2 == "Poison":
        damage = 1
        return damage
    elif type2 == "Ground":
        damage = 2
        return damage
    elif type2 == "Flying":
        damage = 2
        return damage
    elif type2 == "Psychic":
        damage = 1
        return damage
    elif type2 == "Bug":
        damage = 1
        return damage
    elif type2 == "Rock":
        damage = 1
        return damage
    elif type2 == "Ghost":
        damage = 1
        return damage
    elif type2 == "Dragon":
        damage = 2
        return damage
    elif type2 == "Dark":
        damage = 1
        return damage
    elif type2 == "Steel":
        damage = .5
        return damage
    elif type2 == "Fairy":
        damage = 1
        return damage
    else:
        print("Error")

#Narrative: Determines how the Fighting Type Matches up with the other types, and returns
#the effectiveness
def fightingType(type2):
    if type2 == "Normal":
        damage = 2
        return damage
    elif type2 == "Fire":
        damage = 1
        return damage
    elif type2 == "Water":
        damage = 1
        return damage
    elif type2 == "Grass":
        damage = 1
        return damage
    elif type2 == "Electric":
        damage = 1
        return damage
    elif type2 == "Ice":
        damage = 2
        return damage
    elif type2 == "Fighting":
        damage = 1
        return damage
    elif type2 == "Poison":
        damage = .5
        return damage
    elif type2 == "Ground":
        damage = 1
        return damage
    elif type2 == "Flying":
        damage = .5
        return damage
    elif type2 == "Psychic":
        damage = .5
        return damage
    elif type2 == "Bug":
        damage = .5
        return damage
    elif type2 == "Rock":
        damage = 2
        return damage
    elif type2 == "Ghost":
        damage = 0
        return damage
    elif type2 == "Dragon":
        damage = 1
        return damage
    elif type2 == "Dark":
        damage = 2
        return damage
    elif type2 == "Steel":
        damage = 2
        return damage
    elif type2 == "Fairy":
        damage = .5
        return damage
    else:
        print("Error")

#Narrative: Determines how the Poison Type Matches up with the other types, and returns
#the effectiveness
def poisonType(type2):
    if type2 == "Normal":
        damage = 1
        return damage
    elif type2 == "Fire":
        damage = 1
        return damage
    elif type2 == "Water":
        damage = 1
        return damage
    elif type2 == "Grass":
        damage = 2
        return damage
    elif type2 == "Electric":
        damage = 1
        return damage
    elif type2 == "Ice":
        damage = 1
        return damage
    elif type2 == "Fighting":
        damage = 1
        return damage
    elif type2 == "Poison":
        damage = .5
        return damage
    elif type2 == "Ground":
        damage = .5
        return damage
    elif type2 == "Flying":
        damage = 1
        return damage
    elif type2 == "Psychic":
        damage = 1
        return damage
    elif type2 == "Bug":
        damage = 1
        return damage
    elif type2 == "Rock":
        damage = .5
        return damage
    elif type2 == "Ghost":
        damage = .5
        return damage
    elif type2 == "Dragon":
        damage = 1
        return damage
    elif type2 == "Dark":
        damage = 1
        return damage
    elif type2 == "Steel":
        damage = 0
        return damage
    elif type2 == "Fairy":
        damage = 2
        return damage
    else:
        print("Error")

#Narrative: Determines how the Ground Type Matches up with the other types, and returns
#the effectiveness
def groundType(type2):
    if type2 == "Normal":
        damage = 1
        return damage
    elif type2 == "Fire":
        damage = 2
        return damage
    elif type2 == "Water":
        damage = 1
        return damage
    elif type2 == "Grass":
        damage = .5
        return damage
    elif type2 == "Electric":
        damage = 2
        return damage
    elif type2 == "Ice":
        damage = 1
        return damage
    elif type2 == "Fighting":
        damage = 1
        return damage
    elif type2 == "Poison":
        damage = 2
        return damage
    elif type2 == "Ground":
        damage = 1
        return damage
    elif type2 == "Flying":
        damage = 0
        return damage
    elif type2 == "Psychic":
        damage = 1
        return damage
    elif type2 == "Bug":
        damage = .5
        return damage
    elif type2 == "Rock":
        damage = 2
        return damage
    elif type2 == "Ghost":
        damage = 1
        return damage
    elif type2 == "Dragon":
        damage = 1
        return damage
    elif type2 == "Dark":
        damage = 1
        return damage
    elif type2 == "Steel":
        damage = 2
        return damage
    elif type2 == "Fairy":
        damage = 1
        return damage
    else:
        print("Error")

#Narrative: Determines how the Flying Type Matches up with the other types, and returns
#the effectiveness
def flyingType(type2):
    if type2 == "Normal":
        damage = 1
        return damage
    elif type2 == "Fire":
        damage = 1
        return damage
    elif type2 == "Water":
        damage = 1
        return damage
    elif type2 == "Grass":
        damage = 2
        return damage
    elif type2 == "Electric":
        damage = .5
        return damage
    elif type2 == "Ice":
        damage = 1
        return damage
    elif type2 == "Fighting":
        damage = 2
        return damage
    elif type2 == "Poison":
        damage = 1
        return damage
    elif type2 == "Ground":
        damage = 1
        return damage
    elif type2 == "Flying":
        damage = 1
        return damage
    elif type2 == "Psychic":
        damage = 1
        return damage
    elif type2 == "Bug":
        damage = 2
        return damage
    elif type2 == "Rock":
        damage = .5
        return damage
    elif type2 == "Ghost":
        damage = 1
        return damage
    elif type2 == "Dragon":
        damage = 1
        return damage
    elif type2 == "Dark":
        damage = 1
        return damage
    elif type2 == "Steel":
        damage = .5
        return damage
    elif type2 == "Fairy":
        damage = 1
        return damage
    else:
        print("Error")

#Narrative: Determines how the Psychic Type Matches up with the other types, and returns
#the effectiveness
def psychicType(type2):
    if type2 == "Normal":
        damage = 1
        return damage
    elif type2 == "Fire":
        damage = 1
        return damage
    elif type2 == "Water":
        damage = 1
        return damage
    elif type2 == "Grass":
        damage = 1
        return damage
    elif type2 == "Electric":
        damage = 1
        return damage
    elif type2 == "Ice":
        damage = 1
        return damage
    elif type2 == "Fighting":
        damage = 2
        return damage
    elif type2 == "Poison":
        damage = 2
        return damage
    elif type2 == "Ground":
        damage = 1
        return damage
    elif type2 == "Flying":
        damage = 1
        return damage
    elif type2 == "Psychic":
        damage = .5
        return damage
    elif type2 == "Bug":
        damage = 1
        return damage
    elif type2 == "Rock":
        damage = 1
        return damage
    elif type2 == "Ghost":
        damage = 1
        return damage
    elif type2 == "Dragon":
        damage = 1
        return damage
    elif type2 == "Dark":
        damage = 0
        return damage
    elif type2 == "Steel":
        damage = .5
        return damage
    elif type2 == "Fairy":
        damage = 1
        return damage
    else:
        print("Error")

#Narrative: Determines how the Bug Type Matches up with the other types, and returns
#the effectiveness
def bugType(type2):
    if type2 == "Normal":
        damage = 1
        return damage
    elif type2 == "Fire":
        damage = .5
        return damage
    elif type2 == "Water":
        damage = 1
        return damage
    elif type2 == "Grass":
        damage = 2
        return damage
    elif type2 == "Electric":
        damage = 1
        return damage
    elif type2 == "Ice":
        damage = 1
        return damage
    elif type2 == "Fighting":
        damage = .5
        return damage
    elif type2 == "Poison":
        damage = .5
        return damage
    elif type2 == "Ground":
        damage = 1
        return damage
    elif type2 == "Flying":
        damage = .5
        return damage
    elif type2 == "Psychic":
        damage = 2
        return damage
    elif type2 == "Bug":
        damage = 1
        return damage
    elif type2 == "Rock":
        damage = 1
        return damage
    elif type2 == "Ghost":
        damage = .5
        return damage
    elif type2 == "Dragon":
        damage = 1
        return damage
    elif type2 == "Dark":
        damage = 2
        return damage
    elif type2 == "Steel":
        damage = .5
        return damage
    elif type2 == "Fairy":
        damage = .5
        return damage
    else:
        print("Error")

#Narrative: Determines how the Rock Type Matches up with the other types, and returns
#the effectiveness
def rockType(type2):
    if type2 == "Normal":
        damage = 1
        return damage
    elif type2 == "Fire":
        damage = 2
        return damage
    elif type2 == "Water":
        damage = 1
        return damage
    elif type2 == "Grass":
        damage = 1
        return damage
    elif type2 == "Electric":
        damage = 1
        return damage
    elif type2 == "Ice":
        damage = 2
        return damage
    elif type2 == "Fighting":
        damage = .5
        return damage
    elif type2 == "Poison":
        damage = 1
        return damage
    elif type2 == "Ground":
        damage = .5
        return damage
    elif type2 == "Flying":
        damage = 2
        return damage
    elif type2 == "Psychic":
        damage = 1
        return damage
    elif type2 == "Bug":
        damage = 2
        return damage
    elif type2 == "Rock":
        damage = 1
        return damage
    elif type2 == "Ghost":
        damage = 1
        return damage
    elif type2 == "Dragon":
        damage = 1
        return damage
    elif type2 == "Dark":
        damage = 1
        return damage
    elif type2 == "Steel":
        damage = .5
        return damage
    elif type2 == "Fairy":
        damage = 1
        return damage
    else:
        print("Error")

#Narrative: Determines how the Ghost Type Matches up with the other types, and returns
#the effectiveness
def ghostType(type2):
    if type2 == "Normal":
        damage = 0
        return damage
    elif type2 == "Fire":
        damage = 1
        return damage
    elif type2 == "Water":
        damage = 1
        return damage
    elif type2 == "Grass":
        damage = 1
        return damage
    elif type2 == "Electric":
        damage = 1
        return damage
    elif type2 == "Ice":
        damage = 1
        return damage
    elif type2 == "Fighting":
        damage = 1
        return damage
    elif type2 == "Poison":
        damage = 1
        return damage
    elif type2 == "Ground":
        damage = 1
        return damage
    elif type2 == "Flying":
        damage = 1
        return damage
    elif type2 == "Psychic":
        damage = 2
        return damage
    elif type2 == "Bug":
        damage = 1
        return damage
    elif type2 == "Rock":
        damage = 1
        return damage
    elif type2 == "Ghost":
        damage = 2
        return damage
    elif type2 == "Dragon":
        damage = 1
        return damage
    elif type2 == "Dark":
        damage = .5
        return damage
    elif type2 == "Steel":
        damage = 1
        return damage
    elif type2 == "Fairy":
        damage = 1
        return damage
    else:
        print("Error")

#Narrative: Determines how the Dragon Type Matches up with the other types, and returns
#the effectiveness
def dragonType(type2):
    if type2 == "Normal":
        damage = 1
        return damage
    elif type2 == "Fire":
        damage = 1
        return damage
    elif type2 == "Water":
        damage = 1
        return damage
    elif type2 == "Grass":
        damage = 1
        return damage
    elif type2 == "Electric":
        damage = 1
        return damage
    elif type2 == "Ice":
        damage = 1
        return damage
    elif type2 == "Fighting":
        damage = 1
        return damage
    elif type2 == "Poison":
        damage = 1
        return damage
    elif type2 == "Ground":
        damage = 1
        return damage
    elif type2 == "Flying":
        damage = 1
        return damage
    elif type2 == "Psychic":
        damage = 1
        return damage
    elif type2 == "Bug":
        damage = 1
        return damage
    elif type2 == "Rock":
        damage = 1
        return damage
    elif type2 == "Ghost":
        damage = 1
        return damage
    elif type2 == "Dragon":
        damage = 2
        return damage
    elif type2 == "Dark":
        damage = 1
        return damage
    elif type2 == "Steel":
        damage = .5
        return damage
    elif type2 == "Fairy":
        damage = 0
        return damage
    else:
        print("Error")

#Narrative: Determines how the Dark Type Matches up with the other types, and returns
#the effectiveness
def darkType(type2):
    if type2 == "Normal":
        damage = 1
        return damage
    elif type2 == "Fire":
        damage = 1
        return damage
    elif type2 == "Water":
        damage = 1
        return damage
    elif type2 == "Grass":
        damage = 1
        return damage
    elif type2 == "Electric":
        damage = 1
        return damage
    elif type2 == "Ice":
        damage = 1
        return damage
    elif type2 == "Fighting":
        damage = .5
        return damage
    elif type2 == "Poison":
        damage = 1
        return damage
    elif type2 == "Ground":
        damage = 1
        return damage
    elif type2 == "Flying":
        damage = 1
        return damage
    elif type2 == "Psychic":
        damage = 2
        return damage
    elif type2 == "Bug":
        damage = 1
        return damage
    elif type2 == "Rock":
        damage = 1
        return damage
    elif type2 == "Ghost":
        damage = 2
        return damage
    elif type2 == "Dragon":
        damage = 1
        return damage
    elif type2 == "Dark":
        damage = .5
        return damage
    elif type2 == "Steel":
        damage = 1
        return damage
    elif type2 == "Fairy":
        damage = .5
        return damage
    else:
        print("Error")

#Narrative: Determines how the Steel Type Matches up with the other types, and returns
#the effectiveness
def steelType(type2):
    if type2 == "Normal":
        damage = 1
        return damage
    elif type2 == "Fire":
        damage = .5
        return damage
    elif type2 == "Water":
        damage = .5
        return damage
    elif type2 == "Grass":
        damage = 1
        return damage
    elif type2 == "Electric":
        damage = .5
        return damage
    elif type2 == "Ice":
        damage = 2
        return damage
    elif type2 == "Fighting":
        damage = 1
        return damage
    elif type2 == "Poison":
        damage = 1
        return damage
    elif type2 == "Ground":
        damage = 1
        return damage
    elif type2 == "Flying":
        damage = 1
        return damage
    elif type2 == "Psychic":
        damage = 1
        return damage
    elif type2 == "Bug":
        damage = 1
        return damage
    elif type2 == "Rock":
        damage = 2
        return damage
    elif type2 == "Ghost":
        damage = 1
        return damage
    elif type2 == "Dragon":
        damage = 1
        return damage
    elif type2 == "Dark":
        damage = 1
        return damage
    elif type2 == "Steel":
        damage = .5
        return damage
    elif type2 == "Fairy":
        damage = 2
        return damage
    else:
        print("Error")

#Narrative: Determines how the Fairy Type Matches up with the other types, and returns
#the effectiveness
def fairyType(type2):
    if type2 == "Normal":
        damage = 1
        return damage
    elif type2 == "Fire":
        damage = .5
        return damage
    elif type2 == "Water":
        damage = 1
        return damage
    elif type2 == "Grass":
        damage = 1
        return damage
    elif type2 == "Electric":
        damage = 1
        return damage
    elif type2 == "Ice":
        damage = 1
        return damage
    elif type2 == "Fighting":
        damage = 2
        return damage
    elif type2 == "Poison":
        damage = .5
        return damage
    elif type2 == "Ground":
        damage = 1
        return damage
    elif type2 == "Flying":
        damage = 1
        return damage
    elif type2 == "Psychic":
        damage = 1
        return damage
    elif type2 == "Bug":
        damage = 1
        return damage
    elif type2 == "Rock":
        damage = 1
        return damage
    elif type2 == "Ghost":
        damage = 1
        return damage
    elif type2 == "Dragon":
        damage = 2
        return damage
    elif type2 == "Dark":
        damage = 2
        return damage
    elif type2 == "Steel":
        damage = .5
        return damage
    elif type2 == "Fairy":
        damage = 1
        return damage
    else:
        print("Error")