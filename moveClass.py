
class Move:
    #Narrtive: Sets each of the attack attributes
    def __init__(self, name, type, category, power, accuracy):
        self.__name = name
        self.__type = type
        self.__category = category
        self. __power = power
        self.__accuracy = accuracy
    #Narrative: sets the move's name
    def setName(self, name):
        self.__name = name
    #Narrative: sets the move's type
    def setType(self, type):
        self.__type = type
    #Narrative: sets the move's category (either physical or special)
    def setCategory(self, category):
        self.__category = category
    #Narrative: sets the move's attack power
    def setPower(self, power):
        self.__power = power
    #Narrative: sets the move's hit accuracy
    def setAccuracy(self, accuracy):
        self.__accuracy = accuracy
    #Narrative: Returns the move's name
    def getName(self):
        return self.__name
    #Narrative: Returns the move's type
    def getType(self):
        return self.__type
    #Narrative: Returns the move's category (either physical or special
    def getCategory(self):
        return self.__category
    #Narrative: Returns the move's attack power
    def getPower(self):
        return self.__power
    #Narrative: Returns the move's hit accuracy
    def getAccuracy(self):
        return self.__accuracy
    #Narrative: Returns the move's object state
    def __str__(self):
        return "Name: " + self.__name + \
        "\nType : " + self.__type + \
        "\nCategory: " + str(self.__category) + \
        "\nPower: " + str(self.__power) + \
        "\nAccuracy: " + str(self.__accuracy)