import typeChart as type
import random
import math

def setUp(attacker, defender, currentHP, move):
#Determines the Type Effectiveness between the move and the opponent's
# first Type
    typeEffect1 = type.identifyType1(move.getType(), defender.getType1())

#Determines if the opponent has a second typing, and if it does, determines
# the effectiveness between the move and the secondary typing
    if defender.getType2() == "None":
        typeEffect2 = 1
    else:
        typeEffect2 = type.identifyType1(move.getType(), defender.getType2())

#Multiplies the two effectivness's to get the overall type effect
    typeEffect = typeEffect1 * typeEffect2

#Determines if the move is Physical or Special, and sends information to the
# appropriate function
    if move.getCategory() == "Physical":
        infoList = physicalDamage(attacker, defender, currentHP, move, typeEffect)
    else:
        infoList = specialDamage(attacker, defender, currentHP, move, typeEffect)
    return infoList

#Determines base damage using Attack and Defense if the move is Physical
def physicalDamage(attacker, defender, currentHP, move, typeEffect):
    damage = ((110/250) * (attacker.getAttack()/defender.getDefense()) * move.getPower()) + 2
    infoList = calculateDamage(attacker, defender, currentHP, move, typeEffect, damage)
    return infoList

#Determines base damage using Special Attack and Special Defense if the move is
# Special
def specialDamage(attacker, defender, currentHP, move, typeEffect):
    damage = ((110/250) * (attacker.getSpAttack()/defender.getSpDefense()) * move.getPower()) + 2
    infoList = calculateDamage(attacker, defender, currentHP, move, typeEffect, damage)
    return infoList

def calculateDamage(attacker, defender, currentHP, move, typeEffect, damage):
    print(attacker.getName(), "used", move.getName())

#Determines if the move will hit or not, using the move's accuracy stat
    missChance = random.randint(1, 100)
    if missChance <= move.getAccuracy():
        missPrint = ""
        damage = damage * typeEffect

#Implements STAB (Same-Type Attack Bonus) if the moves type is the same as one
# of the attackers types
        if attacker.getType1() == move.getType() or attacker.getType2() == move.getType():
            damage *= 1.5

#Implements Critical Hit, which does extra damage 1/16 times
        critChance = random.randint(1, 16)
        if critChance == 1:
            crit = True
            damage *= 1.5
        else:
            crit = False

#Implements Random Multiplier
        randDamage = random.uniform(.85, 1.000000001)
        damage = damage * randDamage
        damage = math.ceil(damage)

#Prints information
        if crit == True:
            critPrint = "IT'S A CRITICAL HIT!"
        else:
            critPrint = "Not a crit"
        if typeEffect == .5 or typeEffect == .25:
            typePrint = "is not very effective"
        elif typeEffect == 0:
            typePrint = "had no effect"
        elif typeEffect > 1:
            typePrint = "is super-effective"
        else:
            typePrint = "did neutral damage"

#Subtracts the damage dealt from the current HP
        newHP = currentHP - damage

        if newHP <= 0:
            print(defender.getName(), "fainted.")
    else:
        missPrint = "The Move Missed"
        newHP = currentHP
        critPrint = "Not a critical hit"
        typePrint = "The move Missed"

#Returns the new HP value up through the functions
    infoList = [newHP, missPrint, critPrint, typePrint]
    return infoList