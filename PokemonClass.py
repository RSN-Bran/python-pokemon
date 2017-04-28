class Pokemon:
    #Narrative: Sets all of the attributes
    def __init__(self, name, type1, type2, move1, move2, move3, move4, maxHP, attack, defense, spAttack, spDefense,
                 speed, cry, hp):
        self.__name = name
        self.__type1 = type1
        self.__type2 = type2
        self.__move1 = move1
        self.__move2 = move2
        self.__move3 = move3
        self.__move4 = move4
        self.__maxHP = maxHP
        self.__attack = attack
        self.__defense = defense
        self.__spAttack = spAttack
        self.__spDefense = spDefense
        self.__speed = speed
        self.__cry = cry
        self.__hp = hp
    #Narrative: Sets the pokemon's name
    def setName(self, name):
        self.__name = name
    #Narrative: Sets the pokemon's first type
    def setType1(self, type1):
        self.__type1 = type1
    #Narrative: Sets the pokemon's second type
    def setType2(self, type2):
        self.__type2 = type2
    #Narrative: Sets the pokemon's first move name
    def setMove1(self, move1):
        self.__move1 = move1
    #Narrative: Sets the pokemon's second move name
    def setMove2(self, move2):
        self.__move2 = move2
    #Narrative: Sets the pokemon's third move name
    def setMove3(self, move3):
        self.__move3 = move3
    #Narrative: Sets the pokemon's fourth move name
    def setMove4(self, move4):
        self.__move4 = move4
    #Narrative: Sets the pokemon's max HP
    def setMaxHP(self, maxHP):
        self.__maxHP = maxHP
    #Narrative: Sets the pokemon's base attack
    def setAttack(self, attack):
        self.__attack = attack
    #Narrative: Sets the pokemon's base defense
    def setDefense(self, defense):
        self.__defense = defense
    #Narrative: Sets the pokemon's base special attack
    def setSpAttack(self, spAttack):
        self.__spAttack = spAttack
    #Narrative: Sets the pokemon's base special defense
    def setSpDefense(self, spDefense):
        self.__spDefense = spDefense
    #Narrative: Sets the pokemon's speed
    def setSpeed(self, speed):
        self.__speed = speed
    #Narrative: Sets the pokemon's cry sound effect
    def setCry(self, cry):
        self.__cry = cry
    #Narrative: Sets the pokemon's current HP
    def setHP(self, hp):
        self.__hp = hp
    #Narrative: Returns the pokemon's name
    def getName(self):
        return self.__name
    #Narrative: Returns the pokemon's first type
    def getType1(self):
        return self.__type1
    #Narrative: Returns the pokemon's second type
    def getType2(self):
        return self.__type2
    #Narrative: Returns the pokemon's first move
    def getMove1(self):
        return self.__move1
    #Narrative: Returns the pokemon's second move
    def getMove2(self):
        return self.__move2
    #Narrative: Returns the pokemon's third move
    def getMove3(self):
        return self.__move3
    #Narrative: Returns the pokemon's fourth move
    def getMove4(self):
        return self.__move4
    #Narrative: Returns the pokemon's max HP
    def getMaxHP(self):
        return self.__maxHP
    #Narrative: Returns the pokemon's base attack
    def getAttack(self):
        return self.__attack
    #Narrative: Returns the pokemon's base defense
    def getDefense(self):
        return self.__defense
    #Narrative: Returns the pokemon's base special attack
    def getSpAttack(self):
        return self.__spAttack
    #Narrative: Returns the pokemon's base special defense
    def getSpDefense(self):
        return self.__spDefense
    #Narrative: Returns the pokemon's speed
    def getSpeed(self):
        return self.__speed
    #Narrative: Returns the pokemon's cry sound effect
    def getCry(self):
        return self.__cry
    #Narrative: Returns the pokemon's current HP
    def getHP(self):
        return self.__hp
    #Narrative: Returns the pokemon's object state
    def __str__(self):
        return "Name: " + self.__name + \
        "\nType 1: " + self.__type1 + \
        "\nType 2: " + self.__type2 + \
        "\nCurrent HP: " + str(self.__hp) + \
        "\nMax HP: " + str(self.__maxHP) + \
        "\nAttack: " + str(self.__attack) + \
        "\nDefense: " + str(self.__defense) + \
        "\nSpecial Attack: " + str(self.__spAttack) + \
        "\nSpecial Defense: " + str(self.__spDefense) + \
        "\nSpeed: " + str(self.__speed)