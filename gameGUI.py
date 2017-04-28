#Imports imortant modules
from tkinter import *
from tkinter.messagebox import *
import random
import winsound as sound

import PokemonClass as poke
import moveClass as move
import damageCalcGUI as calc


#Establishes each move as a constant
#(Move Name, Move Type, Move Category, Move Power, Move Accuracy)
CRUNCH = move.Move("Crunch", "Dark", "Physical", 80, 100)
WATERFALL = move.Move("Waterfall", "Water", "Physical", 80, 100)
ICEFANG = move.Move("Ice Fang", "Ice", "Physical", 65, 95)
EARTHQUAKE = move.Move("Earthquake", "Ground", "Physical", 100, 100)
DRAGONCLAW = move.Move("Dragon Claw", "Dragon", "Physical", 80, 100)
ROCKSLIDE = move.Move("Rock Slide", "Rock", "Physical", 75, 90)
FLASHCANNON = move.Move("Flash Cannon", "Steel", "Special", 80, 100)
SIGNALBEAM = move.Move("Signal Beam", "Bug", "Special", 75, 100)
THUNDERBOLT = move.Move("Thunderbolt", "Electric", "Special", 90, 100)
TRIATTACK = move.Move("Tri Attack", "Normal", "Special", 80, 100)
SHADOWCLAW = move.Move("Shadow Claw", "Ghost", "Physical", 70, 100)
GUNKSHOT = move.Move("Gunk Shot", "Poison", "Physical", 120, 80)
DARKPULSE = move.Move("Dark Pulse", "Dark", "Special", 80, 100)
BRICKBREAK = move.Move("Brick Break", "Fighting", "Physical", 75, 100)
STRENGTH = move.Move("Strength", "Normal", "Physical", 80, 100)
POISONJAB = move.Move("Poison Jab", "Poison", "Physical", 80, 100)
BOOMBURST = move.Move("Boomburst", "Normal", "Special", 140, 100)
HURRICANE = move.Move("Hurricane", "Flying", "Special", 110, 70)
DRAGONPULSE = move.Move("Dragon Pulse", "Dragon", "Special", 85, 100)
FOCUSBLAST = move.Move("Focus Blast", "Fighting", "Special", 120, 70)
SUPERPOWER = move.Move("SuperPower", "Fighting", "Physical", 120, 100)
SLUDGEBOMB = move.Move("Sludge Bomb", "Poison", "Special", 90, 100)
DAZZLINGGLEAM = move.Move("Dazzling Gleam", "Fairy", "Special", 80, 100)
ENERGYBALL = move.Move("Energy Ball", "Grass", "Special", 90, 100)
EXTRASENSORY = move.Move("Extrasensory", "Psychic", "Special", 80, 100)
FLAMETHROWER = move.Move("Flamethrower", "Fire", "Special", 90, 100)
AIRSLASH = move.Move("Air Slash", "Flying", "Special", 75, 95)
SHADOWBALL = move.Move("Shadow Ball", "Ghost", "Special", 80, 100)
PSYCHIC = move.Move("Psychic", "Psychic", "Special", 90, 100)
ICEBEAM = move.Move("Ice Beam", "Ice", "Special", 90, 100)
STONEEDGE = move.Move("Stone Edge", "Rock", "Physical", 100, 80)
VOLTTACKLE = move.Move("Volt Tackle", "Electric", "Physical", 120, 100)
IRONTAIL = move.Move("Iron Tail", "Steel", "Physical", 100, 75)
SURF = move.Move("Surf", "Water", "Special", 90, 100)
ICICLECRASH = move.Move("Icicle Crash", "Ice", "Physical", 85, 90)
FIREFANG = move.Move("Fire Fang", "Fire", "Physical", 65, 95)
TACKLE = move.Move("Tackle", "Normal", "Physical", 50, 100)
ROCKSMASH = move.Move("Rock Smash", "Fighting", "Physical", 40, 100)
THUNDER = move.Move("Thunder", "Electric", "Special", 110, 70)

#Establishes all the Pokemon as Constants (User Team)
#(Name, Type 1, Type 2, Move 1, Move 2, Move 3, Move 4, HP, Attack, Defense,
#Special Attack, Special Defense, Speed, Cry, HP)
FLYGON = poke.Pokemon("Flygon", "Ground", "Dragon", EARTHQUAKE,
DRAGONCLAW, ROCKSLIDE, SUPERPOWER, 155, 120, 100, 100, 100, 120, "Flygon.wav", 156)
ROSERADE = poke.Pokemon("Roserade", "Grass", "Poison", SLUDGEBOMB,
DAZZLINGGLEAM, ENERGYBALL, EXTRASENSORY, 135, 90, 85, 145, 125, 110, "Roserade.wav", 136)
TOGEKISS = poke.Pokemon("Togekiss", "Fairy", "Flying", FLAMETHROWER,
AIRSLASH, SHADOWBALL, PSYCHIC, 160, 70, 115, 140, 135, 100, "Togekiss.wav", 161)
BULBASAUR = poke.Pokemon("Bulbasaur", "Grass", "Poison", TACKLE,
ENERGYBALL, ROCKSMASH, SLUDGEBOMB, 120, 69, 69, 85, 85, 65, "Bulbasaur.wav", 121)
PIKACHU = poke.Pokemon("Pikachu", "Electric", "None", VOLTTACKLE, IRONTAIL,
SURF, ICICLECRASH, 110, 75, 60, 70, 70, 110, "Pikachu.wav", 111)
TYRANITAR = poke.Pokemon("Tyranitar", "Rock", "Dark", STONEEDGE, CRUNCH,
SHADOWCLAW, FIREFANG, 175, 154, 130, 115, 120, 81, "Tyranitar.wav", 176)

#Establishes all the Pokemon as Constants (Opponent Team)
#(Name, Type 1, Type 2, Move 1, Move 2, Move 3, Move 4, HP, Attack, Defense,
#Special Attack, Special Defense, Speed, Cry, HP)
SHARPEDO = poke.Pokemon("Sharpedo", "Water", "Dark", CRUNCH, WATERFALL,
ICEFANG, EARTHQUAKE, 145, 140, 60, 115, 60, 115, "Sharpedo.wav", 146)
MAGNEZONE = poke.Pokemon("Magnezone", "Electric", "Steel", FLASHCANNON,
SIGNALBEAM, THUNDERBOLT, TRIATTACK, 145, 90, 135, 150, 110, 80, "Magnezone.wav", 146)
BANETTE = poke.Pokemon("Banette", "Ghost", "None", SHADOWCLAW, GUNKSHOT,
THUNDER, DARKPULSE, 139, 135, 85, 103, 83, 85, "Banette.wav", 140)
POLIWRATH = poke.Pokemon("Poliwrath", "Water", "Fighting", BRICKBREAK,
STRENGTH, WATERFALL, POISONJAB, 165, 115, 115, 90, 110, 90, "Poliwrath.wav", 166)
NOIVERN = poke.Pokemon("Noivern", "Flying", "Dragon", BOOMBURST,
HURRICANE, DRAGONPULSE, FOCUSBLAST, 160, 90, 100, 117, 100, 143, "Noivern.wav", 161)
AURORUS = poke.Pokemon("Aurorus", "Rock", "Ice", ICEBEAM, DARKPULSE,
STONEEDGE, EARTHQUAKE, 198, 97, 92, 119, 112, 78, "Aurorus.wav", 199)


class PokemonGUI(Frame):
    #Narrative: Creates all of the frames, imports all of the images, and sets 2 more dummy values
    def __init__(self, AI, HPList, AIHP, player, playerHP):
        Frame.__init__(self)
        self.master.title("Pokemon")
        self.grid()

        #Creates a frame for the images
        #Creates a frame for opponent's health bar
        self.__opponentHealth = Frame(self)
        self.__opponentHealth.grid(row=0, column=0)

        #Creates a frame for opponent's pokemon
        self.__opponentPkmn = Frame(self)
        self.__opponentPkmn.grid(row=0, column=1)

        #Creares a frame for player's pokemon
        self.__playerPkmn = Frame(self)
        self.__playerPkmn.grid(row=1, column=0)

        #Creates a frame for player's health bar
        self.__playerHealth = Frame(self)
        self.__playerHealth.grid(row=1, column=1)

        #Creates a frame for battle text
        self.__middleTextLeft = Frame(self)
        self.__middleTextLeft.grid(row=2, column=0)

        #Creates a frame for text between images and buttons
        self.__middleTextRight = Frame(self)
        self.__middleTextRight.grid(row=2, column=1)

        #Creats a frame for right buttons
        self.__buttonRight = Frame(self)
        self.__buttonRight.grid(row=3, column=0)

        #Creates a frame for left buttons
        self.__buttonLeft = Frame(self)
        self.__buttonLeft.grid(row=3, column=1)

        #Imports all images
        self.__aurorus = PhotoImage(file="aurorus.gif")
        self.__aurorusHealth = PhotoImage(file="aurorusHealth.gif")
        self.__aurorusHealth75 = PhotoImage(file="aurorusHealth75.gif")
        self.__aurorusHealth50 = PhotoImage(file="aurorusHealth50.gif")
        self.__aurorusHealth25 = PhotoImage(file="aurorusHealth25.gif")
        self.__aurorusHealth10 = PhotoImage(file="aurorusHealth10.gif")

        self.__banette = PhotoImage(file="banette.gif")
        self.__banetteHealth = PhotoImage(file="banetteHealth.gif")
        self.__banetteHealth75 = PhotoImage(file="banetteHealth75.gif")
        self.__banetteHealth50 = PhotoImage(file="banetteHealth50.gif")
        self.__banetteHealth25 = PhotoImage(file="banetteHealth25.gif")
        self.__banetteHealth10 = PhotoImage(file="banetteHealth10.gif")

        self.__bulbasaur = PhotoImage(file="bulbasaur.gif")
        self.__bulbasaurHealth = PhotoImage(file="bulbasaurHealth.gif")
        self.__bulbasaurHealth75 = PhotoImage(file="bulbasaurHealth75.gif")
        self.__bulbasaurHealth50 = PhotoImage(file="bulbasaurHealth50.gif")
        self.__bulbasaurHealth25 = PhotoImage(file="bulbasaurHealth25.gif")
        self.__bulbasaurHealth10 = PhotoImage(file="bulbasaurHealth10.gif")

        self.__flygon = PhotoImage(file="flygon.gif")
        self.__flygonHealth = PhotoImage(file="flygonHealth.gif")
        self.__flygonHealth75 = PhotoImage(file="flygonHealth75.gif")
        self.__flygonHealth50 = PhotoImage(file="flygonHealth50.gif")
        self.__flygonHealth25 = PhotoImage(file="flygonHealth25.gif")
        self.__flygonHealth10 = PhotoImage(file="flygonHealth10.gif")

        self.__haris = PhotoImage(file="haris.gif")
        self.__blankTop = PhotoImage(file="blankTop.gif")

        self.__magenzone = PhotoImage(file="magnezone.gif")
        self.__magnezoneHealth = PhotoImage(file="magnezoneHealth.gif")
        self.__magnezoneHealth75 = PhotoImage(file="magnezoneHealth75.gif")
        self.__magnezoneHealth50 = PhotoImage(file="magnezoneHealth50.gif")
        self.__magnezoneHealth25 = PhotoImage(file="magnezoneHealth25.gif")
        self.__magnezoneHealth10 = PhotoImage(file="magnezoneHealth10.gif")

        self.__noivern = PhotoImage(file="noivern.gif")
        self.__noivernHealth = PhotoImage(file="noivernHealth.gif")
        self.__noivernHealth75 = PhotoImage(file="noivernHealth75.gif")
        self.__noivernHealth50 = PhotoImage(file="noivernHealth50.gif")
        self.__noivernHealth25 = PhotoImage(file="noivernHealth25.gif")
        self.__noivernHealth10 = PhotoImage(file="noivernHealth10.gif")

        self.__pikachu = PhotoImage(file="pikachu.gif")
        self.__pikachuHealth = PhotoImage(file="pikachuHealth.gif")
        self.__pikachuHealth75 = PhotoImage(file="pikachuHealth75.gif")
        self.__pikachuHealth50 = PhotoImage(file="pikachuHealth50.gif")
        self.__pikachuHealth25 = PhotoImage(file="pikachuHealth25.gif")
        self.__pikachuHealth10 = PhotoImage(file="pikachuHealth10.gif")

        self.__poliwrath = PhotoImage(file="poliwrath.gif")
        self.__poliwrathHealth = PhotoImage(file="poliwrathHealth.gif")
        self.__poliwrathHealth75 = PhotoImage(file="poliwrathHealth75.gif")
        self.__poliwrathHealth50 = PhotoImage(file="poliwrathHealth50.gif")
        self.__poliwrathHealth25 = PhotoImage(file="poliwrathHealth25.gif")
        self.__poliwrathHealth10 = PhotoImage(file="poliwrathHealth10.gif")

        self.__roserade = PhotoImage(file="roserade.gif")
        self.__roseradeHealth = PhotoImage(file="roseradeHealth.gif")
        self.__roseradeHealth75 = PhotoImage(file="roseradeHealth75.gif")
        self.__roseradeHealth50 = PhotoImage(file="roseradeHealth50.gif")
        self.__roseradeHealth25 = PhotoImage(file="roseradeHealth25.gif")
        self.__roseradeHealth10 = PhotoImage(file="roseradeHealth10.gif")

        self.__sharpedo = PhotoImage(file="sharpedo.gif")
        self.__sharpedoHealth = PhotoImage(file="sharpedoHealth.gif")
        self.__sharpedoHealth75 = PhotoImage(file="sharpedoHealth75.gif")
        self.__sharpedoHealth50 = PhotoImage(file="sharpedoHealth50.gif")
        self.__sharpedoHealth25 = PhotoImage(file="sharpedoHealth25.gif")
        self.__sharpedoHealth10 = PhotoImage(file="sharpedoHealth10.gif")

        self.__togekiss = PhotoImage(file="togekiss.gif")
        self.__togekissHealth = PhotoImage(file="togekissHealth.gif")
        self.__togekissHealth75 = PhotoImage(file="togekissHealth75.gif")
        self.__togekissHealth50 = PhotoImage(file="togekissHealth50.gif")
        self.__togekissHealth25 = PhotoImage(file="togekissHealth25.gif")
        self.__togekissHealth10 = PhotoImage(file="togekissHealth10.gif")

        self.__trainer = PhotoImage(file="trainer.gif")
        self.__playerPokeballs = PhotoImage(file="playerPokeballs.gif")
        self.__blankBottom = PhotoImage(file="blankBottom.gif")

        self.__tyranitar = PhotoImage(file="tyranitar.gif")
        self.__tyranitarHealth = PhotoImage(file="tyranitarHealth.gif")
        self.__tyranitarHealth75 = PhotoImage(file="tyranitarHealth75.gif")
        self.__tyranitarHealth50 = PhotoImage(file="tyranitarHealth50.gif")
        self.__tyranitarHealth25 = PhotoImage(file="tyranitarHealth25.gif")
        self.__tyranitarHealth10 = PhotoImage(file="tyranitarHealth10.gif")


        self.startingPoint(AI, HPList, AIHP, player, playerHP)


    #Narrative: Selects new pokemon for AI
    def startingPoint(self, AI, HPList, AIHP, player, playerHP):

        #Establishes a list of opponent Pokemon, and picks one using a random number
        #function. Makes sure the chosen Pokemon has HP before continuing
        if AIHP <= 0:
            checkCtr = 0
            while checkCtr == 0:
                opponentTeam = [SHARPEDO, MAGNEZONE, BANETTE, POLIWRATH, NOIVERN, AURORUS]
                chooseNum = random.randint(0,5)
                AI = opponentTeam[chooseNum]
                if AI == SHARPEDO:
                    if HPList[6] > 0:
                        self.__opponentPkmn.destroy()
                        self.__opponentPkmn = Frame(self)
                        self.__opponentPkmn.grid(row=0, column=1)
                        AIPokemon = Label(self.__opponentPkmn, image=self.__sharpedo)
                        AIPokemon.grid()

                        self.__opponentHealth.destroy()
                        self.__opponentHealth = Frame(self)
                        self.__opponentHealth.grid(row=0, column=0)
                        AIHealth = Label(self.__opponentHealth, image=self.__sharpedoHealth)
                        AIHealth.grid()

                        checkCtr = 1
                if AI == MAGNEZONE:
                    if HPList[7] > 0:
                        self.__opponentPkmn.destroy()
                        self.__opponentPkmn = Frame(self)
                        self.__opponentPkmn.grid(row=0, column=1)
                        AIPokemon = Label(self.__opponentPkmn, image=self.__magenzone)
                        AIPokemon.grid()

                        self.__opponentHealth.destroy()
                        self.__opponentHealth = Frame(self)
                        self.__opponentHealth.grid(row=0, column=0)
                        AIHealth = Label(self.__opponentHealth, image=self.__magnezoneHealth)
                        AIHealth.grid()

                        checkCtr = 1
                if AI == BANETTE:
                    if HPList[8] > 0:
                        self.__opponentPkmn.destroy()
                        self.__opponentPkmn = Frame(self)
                        self.__opponentPkmn.grid(row=0, column=1)
                        AIPokemon = Label(self.__opponentPkmn, image=self.__banette)
                        AIPokemon.grid()

                        self.__opponentHealth.destroy()
                        self.__opponentHealth = Frame(self)
                        self.__opponentHealth.grid(row=0, column=0)
                        AIHealth = Label(self.__opponentHealth, image=self.__banetteHealth)
                        AIHealth.grid()

                        checkCtr = 1
                if AI == POLIWRATH:
                    if HPList[9] > 0:
                        self.__opponentPkmn.destroy()
                        self.__opponentPkmn = Frame(self)
                        self.__opponentPkmn.grid(row=0, column=1)
                        AIPokemon = Label(self.__opponentPkmn, image=self.__poliwrath)
                        AIPokemon.grid()

                        self.__opponentHealth.destroy()
                        self.__opponentHealth = Frame(self)
                        self.__opponentHealth.grid(row=0, column=0)
                        AIHealth = Label(self.__opponentHealth, image=self.__poliwrathHealth)
                        AIHealth.grid()

                        checkCtr = 1
                if AI == NOIVERN:
                    if HPList[10] > 0:
                        self.__opponentPkmn.destroy()
                        self.__opponentPkmn = Frame(self)
                        self.__opponentPkmn.grid(row=0, column=1)
                        AIPokemon = Label(self.__opponentPkmn, image=self.__noivern)
                        AIPokemon.grid()

                        self.__opponentHealth.destroy()
                        self.__opponentHealth = Frame(self)
                        self.__opponentHealth.grid(row=0, column=0)
                        AIHealth = Label(self.__opponentHealth, image=self.__noivernHealth)
                        AIHealth.grid()

                        checkCtr = 1
                if AI == AURORUS:
                    if HPList[11] > 0:
                        self.__opponentPkmn.destroy()
                        self.__opponentPkmn = Frame(self)
                        self.__opponentPkmn.grid(row=0, column=1)
                        AIPokemon = Label(self.__opponentPkmn, image=self.__aurorus)
                        AIPokemon.grid()

                        self.__opponentHealth.destroy()
                        self.__opponentHealth = Frame(self)
                        self.__opponentHealth.grid(row=0, column=0)
                        AIHealth = Label(self.__opponentHealth, image=self.__aurorusHealth)
                        AIHealth.grid()

                        checkCtr = 1

        #Sets AI pokemon
        if AI == SHARPEDO:
            AIHP = HPList[6]
        elif AI == MAGNEZONE:
            AIHP = HPList[7]
        elif AI == BANETTE:
            AIHP = HPList[8]
        elif AI == POLIWRATH:
            AIHP = HPList[9]
        elif AI == NOIVERN:
            AIHP = HPList[10]
        else:
            AIHP = HPList[11]

        self.phaseOne(AI, HPList, AIHP, player, playerHP)

    #Narrative: Checks to see if this is the first time the player is running the code to display certain text, displays
    #Ribic's pokemon, checks if player's pokemon is dead or not and send the game to the appropriate function
    def phaseOne(self, AI, HPList, AIHP, player, playerHP):
        AISentOut = Label(self, text="Dummy")
        initialBattle = Label(self, text="Dummy")
        sendPokemon = Label(self, text="Dummy")

        #Acknwoledges that if the player value is "Dummy", it is the first turn of the
        #battle, states entry message
        if player == "Dummy":
            initialBattle = Label(self.__middleTextRight, text="Pycharmer Ribic wants to battle!")
            initialBattle.grid(row=0, column=0)
            print("Pycharmer Ribic wants to battle!")

            trainer = Label(self.__playerPkmn, image=self.__trainer)
            trainer.grid()

            trainerPokeballs = Label(self.__playerHealth, image=self.__playerPokeballs)
            trainerPokeballs.grid()



        #Acknowledges that it's an AI Pokemon's first turn on the field, as it's current
        #HP is greater than it's max HP. Decreases HP to correct value and states
        #entry message and plays cry
        if AI.getMaxHP() < AIHP:
            AIHP -= 1

            AISentOut = Label(self.__middleTextRight, text="PyCharmer Ribic sent out: " + AI.getName())
            AISentOut.grid(row=2, column=0)
            print("PyCharmer Ribic sent out", AI.getName())
            #Winsound: allows a python program to play a .wav sound file on windows OS. Format is:
            # PlaySond("FileName.wav", winsound.SND_FILENAME). Found on StackOverFlow.com
            sound.PlaySound(AI.getCry(), sound.SND_FILENAME)


        #If the player's Pokemon's HP is less than or equal to 0, they must choose a
        #Pokemon to use, sent to appropriate Function
        if playerHP <= 0:
            self.pickPokemon(AI, HPList, AIHP, AISentOut, initialBattle)
        #If Pokemon is still useable, goes straight to move picking
        else:
            self.pickMove(player, playerHP, AI, AIHP, HPList, sendPokemon, AISentOut)


    #Narrative: Asks which pokemon the player would like to send out, checks if the selected pokemon is fainted or not
    #and either sends pokemon to a display function or a message box letting user know the pokemon is fainted
    def pickPokemon(self, AI, HPList, AIHP, AISentOut, initialBattle):
        pokemonSelect = Label(self.__middleTextRight, text = "Pick a Pokemon")
        pokemonSelect.grid(row=3, column=0)

        #Establishes 6 Buttons for each Pokemon, establishes the picked Pokemon Button
        #as the users Pokemon, and sends that Pokemon, it's health, and all button
        #values as a list to the next Function
        #Lambda Functions: Act as a one line function and allows us to send buttons as arguements. Format:
        # lambda: *function*. Found on StackOverFlow.com
        Button1 = Button(self.__buttonLeft, text = "Flygon",
                        command = lambda: self.deletePokemon(FLYGON, HPList[0], AI, AIHP, HPList,
                                                              [Button1, Button2, Button3, Button4, initialBattle,
                                                               AISentOut, Button5, Button6, AISentOut, pokemonSelect]))
        Button1.grid(row = 1, column = 0, columnspan = 2)

        Button2 = Button(self.__buttonLeft, text = "Roserade",
                         command = lambda: self.deletePokemon(ROSERADE, HPList[1], AI, AIHP, HPList,
                                                              [Button1, Button2, Button3, Button4, initialBattle,
                                                               AISentOut, Button5, Button6, AISentOut, pokemonSelect]))
        Button2.grid(row = 2, column = 0, columnspan = 2)

        Button3 = Button(self.__buttonLeft, text = "Togekiss",
                         command = lambda: self.deletePokemon(TOGEKISS, HPList[2], AI, AIHP, HPList,
                                                              [Button1, Button2, Button3, Button4, initialBattle,
                                                               AISentOut, Button5, Button6, AISentOut, pokemonSelect]))
        Button3.grid(row = 3, column = 0, columnspan = 2)

        Button4 = Button(self.__buttonRight, text = "Bulbasaur",
                         command = lambda: self.deletePokemon(BULBASAUR, HPList[3], AI, AIHP, HPList,
                                                              [Button1, Button2, Button3, Button4, initialBattle,
                                                               AISentOut, Button5, Button6, AISentOut, pokemonSelect]))
        Button4.grid(row = 1, column = 0, columnspan = 2)

        Button5 = Button(self.__buttonRight, text = "Pikachu",
                         command = lambda: self.deletePokemon(PIKACHU, HPList[4], AI, AIHP, HPList,
                                                              [Button1, Button2, Button3, Button4, initialBattle,
                                                               AISentOut, Button5, Button6, AISentOut, pokemonSelect]))
        Button5.grid(row = 2, column = 0, columnspan = 2)

        Button6 = Button(self.__buttonRight, text = "Tyranitar",
                         command = lambda: self.deletePokemon(TYRANITAR, HPList[5], AI, AIHP, HPList,
                                                              [Button1, Button2, Button3, Button4, initialBattle,
                                                               AISentOut, Button5, Button6, AISentOut, pokemonSelect]))
        Button6.grid(row = 3, column = 0, columnspan = 2)


    #Narrative: Deletes the player pokemon frame to rid of any previous images in it and creates a new frame to display
    #the selected pokemon. Also displays a dialogue if pokemon fainted and updates ribic's pokemon image
    def deletePokemon(self, player, playerHP, AI, AIHP, HPList, widgetList):
        #Destroys all Button/Text Values
        for item in widgetList:
            item.destroy()

        sendPokemon = Label(self, text="Dummy")
        AISentOut = Label(self, text="Dummy")
        initialBattle = Label(self, text="Dummy")

        self.__middleTextRight.destroy()
        self.__middleTextRight = Frame(self)
        self.__middleTextRight.grid(row=2, column=1)
        self.__middleTextLeft.destroy()
        self.__middleTextLeft = Frame(self)
        self.__middleTextLeft.grid(row=2,column=0)

        #Determines if the picked Pokemon is useable, based on it's current HP, if it
        #isn't, the user is sent back to starting  point, otherwise, the user is
        #sent to move picker
        if player == FLYGON:
            if HPList[0] <= 0:
                print("This Pokemon Can't Fight")
                self.cantFight()
                self.pickPokemon(AI, HPList, AIHP, AISentOut, initialBattle)
            else:
                if player.getMaxHP() < playerHP:
                    playerHP -= 1
                    sendPokemon = Label(self.__middleTextRight, text="GO Flygon")
                    sendPokemon.grid(row=0)
                    print("GO Flygon!")

                self.__playerPkmn.destroy()
                self.__playerPkmn = Frame(self)
                self.__playerPkmn.grid(row=1, column=0)
                playerPokemon = Label(self.__playerPkmn, image=self.__flygon)
                playerPokemon.grid(row=0, column=0)
                sound.PlaySound(player.getCry(), sound.SND_FILENAME)

                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                playerHealth = Label(self.__playerHealth, image=self.__flygonHealth)
                playerHealth.grid()

        elif player == ROSERADE:
            if HPList[1] <= 0:
                print("This Pokemon Can't Fight")
                self.cantFight()
                self.pickPokemon(AI, HPList, AIHP, AISentOut, initialBattle)
            else:
                if player.getMaxHP() < playerHP:
                    playerHP -= 1
                    sendPokemon = Label(self.__middleTextRight, text="GO Roserade!")
                    sendPokemon.grid(row=0)
                    print("GO Roserade!")

                self.__playerPkmn.destroy()
                self.__playerPkmn = Frame(self)
                self.__playerPkmn.grid(row=1, column=0)
                playerPokemon = Label(self.__playerPkmn, image=self.__roserade)
                playerPokemon.grid(row=0, column=0)
                sound.PlaySound(player.getCry(), sound.SND_FILENAME)

                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                playerHealth = Label(self.__playerHealth, image=self.__roseradeHealth)
                playerHealth.grid()

        elif player == TOGEKISS:
            if HPList[2] <= 0:
                print("This Pokemon Can't Fight")
                self.cantFight()
                self.pickPokemon(AI, HPList, AIHP, AISentOut, initialBattle)
            else:
                if player.getMaxHP() < playerHP:
                    playerHP -= 1
                    sendPokemon = Label(self.__middleTextRight, text="GO Togekiss!")
                    sendPokemon.grid(row=0)
                    print("GO Togekiss!")

                self.__playerPkmn.destroy()
                self.__playerPkmn = Frame(self)
                self.__playerPkmn.grid(row=1, column=0)
                playerPokemon = Label(self.__playerPkmn, image=self.__togekiss)
                playerPokemon.grid(row=0, column=0)
                sound.PlaySound(player.getCry(), sound.SND_FILENAME)

                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                playerHealth = Label(self.__playerHealth, image=self.__togekissHealth)
                playerHealth.grid()

        elif player == BULBASAUR:
            if HPList[3] <= 0:
                print("This Pokemon Can't Fight")
                self.cantFight()
                self.pickPokemon(AI, HPList, AIHP, AISentOut, initialBattle)
            else:
                if player.getMaxHP() < playerHP:
                    playerHP -= 1
                    sendPokemon = Label(self.__middleTextRight, text="GO Bulbasaur!")
                    sendPokemon.grid(row=0)
                    print("GO Bulbasaur!")

                self.__playerPkmn.destroy()
                self.__playerPkmn = Frame(self)
                self.__playerPkmn.grid(row=1, column=0)
                playerPokemon = Label(self.__playerPkmn, image=self.__bulbasaur)
                playerPokemon.grid(row=0, column=0)
                sound.PlaySound(player.getCry(), sound.SND_FILENAME)

                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                playerHealth = Label(self.__playerHealth, image=self.__bulbasaurHealth)
                playerHealth.grid()

        elif player == PIKACHU:
            if HPList[4] <= 0:
                print("This Pokemon Can't Fight")
                self.cantFight()
                self.pickPokemon(AI, HPList, AIHP, AISentOut, initialBattle)
            else:
                if player.getMaxHP() < playerHP:
                    playerHP -= 1
                    sendPokemon = Label(self.__middleTextRight, text="GO Pikachu!")
                    sendPokemon.grid(row=0)
                    print("GO Pikachu!")

                self.__playerPkmn.destroy()
                self.__playerPkmn = Frame(self)
                self.__playerPkmn.grid(row=1, column=0)
                playerPokemon = Label(self.__playerPkmn, image=self.__pikachu)
                playerPokemon.grid(row=0, column=0)
                sound.PlaySound(player.getCry(), sound.SND_FILENAME)

                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                playerHealth = Label(self.__playerHealth, image=self.__pikachuHealth)
                playerHealth.grid()

        elif player == TYRANITAR:
            if HPList[5] <= 0:
                print("This Pokemon Can't Fight")
                self.cantFight()
                self.pickPokemon(AI, HPList, AIHP, AISentOut, initialBattle)
            else:
                if player.getMaxHP() < playerHP:
                    playerHP -= 1
                    sendPokemon = Label(self.__middleTextRight, text="GO Tyranitar!")
                    sendPokemon.grid(row=0)
                    print("GO Tyranitar!")

                self.__playerPkmn.destroy()
                self.__playerPkmn = Frame(self)
                self.__playerPkmn.grid(row=1, column=0)
                playerPokemon = Label(self.__playerPkmn, image=self.__tyranitar)
                playerPokemon.grid(row=0, column=0)
                sound.PlaySound(player.getCry(), sound.SND_FILENAME)

                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                playerHealth = Label(self.__playerHealth, image=self.__tyranitarHealth)
                playerHealth.grid()
        else:
            #Pass: Allows a program to have an else statement at the end of an if-elif-else statement without the else
            # statement doing anything. Format: pass. Found on StackOverFlow
            pass

        if AI == SHARPEDO:
            self.__opponentPkmn.destroy()
            self.__opponentPkmn = Frame(self)
            self.__opponentPkmn.grid(row=0, column=1)
            AIPokemon = Label(self.__opponentPkmn, image=self.__sharpedo)
            AIPokemon.grid()

        elif AI == MAGNEZONE:
            self.__opponentPkmn.destroy()
            self.__opponentPkmn = Frame(self)
            self.__opponentPkmn.grid(row=0, column=1)
            AIPokemon = Label(self.__opponentPkmn, image=self.__magenzone)
            AIPokemon.grid()

        elif AI == BANETTE:
            self.__opponentPkmn.destroy()
            self.__opponentPkmn = Frame(self)
            self.__opponentPkmn.grid(row=0, column=1)
            AIPokemon = Label(self.__opponentPkmn, image=self.__banette)
            AIPokemon.grid()

        elif AI == POLIWRATH:
            self.__opponentPkmn.destroy()
            self.__opponentPkmn = Frame(self)
            self.__opponentPkmn.grid(row=0, column=1)
            AIPokemon = Label(self.__opponentPkmn, image=self.__poliwrath)
            AIPokemon.grid()

        elif AI == NOIVERN:
            self.__opponentPkmn.destroy()
            self.__opponentPkmn = Frame(self)
            self.__opponentPkmn.grid(row=0, column=1)
            AIPokemon = Label(self.__opponentPkmn, image=self.__noivern)
            AIPokemon.grid()

        elif AI == AURORUS:
            self.__opponentPkmn.destroy()
            self.__opponentPkmn = Frame(self)
            self.__opponentPkmn.grid(row=0, column=1)
            AIPokemon = Label(self.__opponentPkmn, image=self.__aurorus)
            AIPokemon.grid()

        else:
            pass

        self.pickMove(player, playerHP, AI, AIHP, HPList, sendPokemon, AISentOut)


    #Narrative: Displays the dialogue box for if the pokemon is fainted
    def cantFight(self):
        showinfo(message = "This pokemon fainted and cannot battle", parent = self)


    #Narrative: Displays each of the pokemon's moves and sends the move info to the useMove function
    def pickMove(self, player, playerHP, AI, AIHP, HPList, sendPokemon, AISentOut):
        if player.getHP() > 0:
            movePick = Label(self.__middleTextRight, text = "Pick a Move")
            movePick.grid(row=3, column=0)
            #Establishes Buttons for each move, sends all previous information, and
            #chosen move to the next function
            Move1 = Button(self.__buttonLeft, text = player.getMove1().getName(),
                           command = lambda: self.useMove(player, playerHP, player.getMove1(), AI, AIHP,
                                                            [Move1, Move2, Move3, Move4, movePick, sendPokemon,
                                                             AISentOut], HPList))
            Move1.grid(row = 1, column = 0, columnspan = 3)

            Move2 = Button(self.__buttonLeft, text = player.getMove2().getName(),
                           command = lambda: self.useMove(player, playerHP, player.getMove2(), AI, AIHP,
                                                            [Move1, Move2, Move3, Move4, movePick, sendPokemon,
                                                             AISentOut], HPList))
            Move2.grid(row = 2, column = 0, columnspan = 3)

            Move3 = Button(self.__buttonRight, text = player.getMove3().getName(),
                           command = lambda: self.useMove(player, playerHP, player.getMove3(), AI, AIHP,
                                                          [Move1, Move2, Move3, Move4, movePick, sendPokemon,
                                                           AISentOut], HPList))
            Move3.grid(row = 1, column = 4, columnspan = 3)

            Move4 = Button(self.__buttonRight, text = player.getMove4().getName(),
                           command = lambda: self.useMove(player, playerHP, player.getMove4(), AI, AIHP,
                                                            [Move1, Move2, Move3, Move4, movePick, sendPokemon,
                                                             AISentOut], HPList))
            Move4.grid(row = 2, column = 4, columnspan = 3)


    #Narrative: Sends all of the info to the damage calculator and updates the pokemon's HP with their new HP. Also
    #checks if either player is defeated
    def useMove(self, player, playerHP, playerMove, AI, AIHP, moveList, HPList):
        #Destroys Buttons/Text
        for item in moveList:
            item.destroy()

        self.__middleTextRight.destroy()
        self.__middleTextRight = Frame(self)
        self.__middleTextRight.grid(row=2,column=1)

        #AI picks a move using a random number function
        randMove = random.randint(1,4)
        if randMove == 1:
            AIMove = AI.getMove1()
        elif randMove == 2:
            AIMove = AI.getMove2()
        elif randMove == 3:
            AIMove = AI.getMove3()
        else:
            AIMove = AI.getMove4()

        #infoList1 is when player attacks and holds AI's new hp
        #infoList2 is when AI attacks and holds player's new hp
        #Determines which Pokemon will go first by using speed values
        if player.getSpeed() > AI.getSpeed():
            infoList1 = calc.setUp(player, AI, AIHP, playerMove)
            AIHP = infoList1[0]
            #Makes sure the slower Pokemon hasn't fainted, before allowing it to move
            if infoList1[0] >= 0:
                infoList2 = calc.setUp(AI, player, playerHP, AIMove)
                playerHP = infoList2[0]

        else:
            infoList2 = calc.setUp(AI, player, playerHP, AIMove)
            playerHP = infoList2[0]
            if infoList2[0] >= 0:
                infoList1 = calc.setUp(player, AI, AIHP, playerMove)
                AIHP = infoList1[0]

        #Re-establishes HP Variables, as values in the list for user
        if player == FLYGON:
            HPList[0] = playerHP
            player.setHP(playerHP)
        elif player == ROSERADE:
            HPList [1] = playerHP
            player.setHP(playerHP)
        elif player == TOGEKISS:
            HPList [2] = playerHP
            player.setHP(playerHP)
        elif player == BULBASAUR:
            HPList [3] = playerHP
            player.setHP(playerHP)
        elif player == PIKACHU:
            HPList [4] = playerHP
            player.setHP(playerHP)
        elif player == TYRANITAR:
            HPList[5] = playerHP
            player.setHP(playerHP)
        else:
            pass

        #Re-establishes HP Variables, as values in the list for AI
        if AI == SHARPEDO:
            HPList[6] = AIHP
            AI.setHP(AIHP)
        elif AI == MAGNEZONE:
            HPList[7] = AIHP
            AI.setHP(AIHP)
        elif AI == BANETTE:
            HPList[8] = AIHP
            AI.setHP(AIHP)
        elif AI == POLIWRATH:
            HPList[9] = AIHP
            AI.setHP(AIHP)
        elif AI == NOIVERN:
            HPList[10] = AIHP
            AI.setHP(AIHP)
        elif AI == AURORUS:
            HPList[11] = AIHP
            AI.setHP(AIHP)
        else:
            pass


        self.__middleTextLeft.destroy()
        self.__middleTextLeft = Frame(self)
        self.__middleTextLeft.grid(row=2, column=0)

        self.__middleTextRight.destroy()
        self.__middleTextRight = Frame(self)
        self.__middleTextRight.grid(row=2, column=0)

        try:
            self.__middleTextLeft.destroy()
            self.__middleTextLeft = Frame(self)
            self.__middleTextLeft.grid(row=2,column=0)

            #Display's info about the pokemon's hits such as it's effectiveness, whether or not it was a critcal hit, and
            #the defending pokemon's new health
            textPlayerHealth = Label(self.__middleTextLeft, text=player.getName() + " has " + str(player.getHP()) +\
                                                                    " out of " + str(player.getMaxHP()) + " health left")
            textPlayerHealth.grid(row=0,column=0)
            if infoList2[1] == "The Move Missed":
                textAIMoveHit = Label(self.__middleTextLeft, text=AI.getName() + "'s attack missed")
                textAIMoveHit.grid(row=1,column=0)
            else:
                textAIMoveHit = Label(self.__middleTextLeft, text=AI.getName() + "'s attack was " + infoList2[3] +\
                                                                " (" + infoList2[2] + ")")
                textAIMoveHit.grid(row=1,column=0)
        except UnboundLocalError as err:
            print("ERROR: ", err)

        try:
            self.__middleTextRight.destroy()
            self.__middleTextRight = Frame(self)
            self.__middleTextRight.grid(row=2,column=1)

            textAIHealth = Label(self.__middleTextRight, text=AI.getName() + " has " + str(AI.getHP()) +\
                                                                " out of " + str(AI.getMaxHP()) + " health left")
            textAIHealth.grid(row=0,column=0)
            if infoList1[1] == "The Move Missed":
                textPlayerMoveHit = Label(self.__middleTextRight, text=player.getName() + "'s attack missed")
                textPlayerMoveHit.grid(row=1,column=0)
            else:
                textPlayerMoveHit = Label(self.__middleTextRight, text=player.getName() + "'s attack was " + infoList1[3] +\
                                                                " (" + infoList1[2] + ")")
                textPlayerMoveHit.grid(row=1,column=0)

        except UnboundLocalError as err:
            print("ERROR: ", err)

        if player == FLYGON:
            if player.getHP() <= (player.getMaxHP() * .10):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__flygonHealth10)
                pokemonHealth.grid()

            elif player.getHP() <= (player.getMaxHP() * .25):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__flygonHealth25)
                pokemonHealth.grid()

            elif player.getHP() <= (player.getMaxHP() * .50):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__flygonHealth50)
                pokemonHealth.grid()

            elif player.getHP() <= (player.getMaxHP() * .75):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__flygonHealth75)
                pokemonHealth.grid()
            else:
                pass

        elif player == BULBASAUR:
            if player.getHP() <= (player.getMaxHP() * .10):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__bulbasaurHealth10)
                pokemonHealth.grid()

            elif player.getHP() <= (player.getMaxHP() * .25):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__bulbasaurHealth25)
                pokemonHealth.grid()

            elif player.getHP() <= (player.getMaxHP() * .50):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__bulbasaurHealth50)
                pokemonHealth.grid()

            elif player.getHP() <= (player.getMaxHP() * .75):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__bulbasaurHealth75)
                pokemonHealth.grid()
            else:
                pass

        elif player == PIKACHU:
            if player.getHP() <= (player.getMaxHP() * .10):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__pikachuHealth10)
                pokemonHealth.grid()

            elif player.getHP() <= (player.getMaxHP() * .25):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__pikachuHealth25)
                pokemonHealth.grid()

            elif player.getHP() <= (player.getMaxHP() * .50):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__pikachuHealth50)
                pokemonHealth.grid()

            elif player.getHP() <= (player.getMaxHP() * .75):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__pikachuHealth75)
                pokemonHealth.grid()
            else:
                pass

        elif player == ROSERADE:
            if player.getHP() <= (player.getMaxHP() * .10):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__roseradeHealth10)
                pokemonHealth.grid()

            elif player.getHP() <= (player.getMaxHP() * .25):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__roseradeHealth25)
                pokemonHealth.grid()

            elif player.getHP() <= (player.getMaxHP() * .50):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__roseradeHealth50)
                pokemonHealth.grid()

            elif player.getHP() <= (player.getMaxHP() * .75):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__roseradeHealth75)
                pokemonHealth.grid()
            else:
                pass

        elif player == TOGEKISS:
            if player.getHP() <= (player.getMaxHP() * .10):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__togekissHealth10)
                pokemonHealth.grid()

            elif player.getHP() <= (player.getMaxHP() * .25):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__togekissHealth25)
                pokemonHealth.grid()

            elif player.getHP() <= (player.getMaxHP() * .50):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__togekissHealth50)
                pokemonHealth.grid()

            elif player.getHP() <= (player.getMaxHP() * .75):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__togekissHealth75)
                pokemonHealth.grid()
            else:
                pass

        elif player == TYRANITAR:
            if player.getHP() <= (player.getMaxHP() * .10):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__tyranitarHealth10)
                pokemonHealth.grid()

            elif player.getHP() <= (player.getMaxHP() * .25):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__tyranitarHealth25)
                pokemonHealth.grid()

            elif player.getHP() <= (player.getMaxHP() * .50):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__tyranitarHealth50)
                pokemonHealth.grid()

            elif player.getHP() <= (player.getMaxHP() * .75):
                self.__playerHealth.destroy()
                self.__playerHealth = Frame(self)
                self.__playerHealth.grid(row=1, column=1)
                pokemonHealth = Label(self.__playerHealth, image=self.__tyranitarHealth75)
                pokemonHealth.grid()
            else:
                pass
        else:
            pass

        if AI == AURORUS:
            if AI.getHP() <= (AI.getMaxHP() * .10):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__aurorusHealth10)
                pokemonHealth.grid()

            elif AI.getHP() <= (AI.getMaxHP() * .25):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__aurorusHealth25)
                pokemonHealth.grid()

            elif AI.getHP() <= (AI.getMaxHP() * .50):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__aurorusHealth50)
                pokemonHealth.grid()

            elif AI.getHP() <= (AI.getMaxHP() * .75):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__aurorusHealth75)
                pokemonHealth.grid()
            else:
                pass

        elif AI == BANETTE:
            if AI.getHP() <= (AI.getMaxHP() * .10):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__banetteHealth10)
                pokemonHealth.grid()

            elif AI.getHP() <= (AI.getMaxHP() * .25):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__banetteHealth25)
                pokemonHealth.grid()

            elif AI.getHP() <= (AI.getMaxHP() * .50):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__banetteHealth50)
                pokemonHealth.grid()

            elif AI.getHP() <= (AI.getMaxHP() * .75):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__banetteHealth75)
                pokemonHealth.grid()
            else:
                pass

        elif AI == MAGNEZONE:
            if AI.getHP() <= (AI.getMaxHP() * .10):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__magnezoneHealth10)
                pokemonHealth.grid()

            elif AI.getHP() <= (AI.getMaxHP() * .25):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__magnezoneHealth25)
                pokemonHealth.grid()

            elif AI.getHP() <= (AI.getMaxHP() * .50):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__magnezoneHealth50)
                pokemonHealth.grid()

            elif AI.getHP() <= (AI.getMaxHP() * .75):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__magnezoneHealth75)
                pokemonHealth.grid()
            else:
                pass

        elif AI == NOIVERN:
            if AI.getHP() <= (AI.getMaxHP() * .10):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__noivernHealth10)
                pokemonHealth.grid()

            elif AI.getHP() <= (AI.getMaxHP() * .25):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__noivernHealth25)
                pokemonHealth.grid()

            elif AI.getHP() <= (AI.getMaxHP() * .50):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__noivernHealth50)
                pokemonHealth.grid()

            elif AI.getHP() <= (AI.getMaxHP() * .75):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__noivernHealth75)
                pokemonHealth.grid()
            else:
                pass

        elif AI == POLIWRATH:
            if AI.getHP() <= (AI.getMaxHP() * .10):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__poliwrathHealth10)
                pokemonHealth.grid()

            elif AI.getHP() <= (AI.getMaxHP() * .25):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__poliwrathHealth25)
                pokemonHealth.grid()

            elif AI.getHP() <= (AI.getMaxHP() * .50):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__poliwrathHealth50)
                pokemonHealth.grid()

            elif AI.getHP() <= (AI.getMaxHP() * .75):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__poliwrathHealth75)
                pokemonHealth.grid()
            else:
                pass

        elif AI == SHARPEDO:
            if AI.getHP() <= (AI.getMaxHP() * .10):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__sharpedoHealth10)
                pokemonHealth.grid()

            elif AI.getHP() <= (AI.getMaxHP() * .25):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__sharpedoHealth25)
                pokemonHealth.grid()

            elif AI.getHP() <= (AI.getMaxHP() * .50):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__sharpedoHealth50)
                pokemonHealth.grid()

            elif AI.getHP() <= (AI.getMaxHP() * .75):
                self.__opponentHealth.destroy()
                self.__opponentHealth = Frame(self)
                self.__opponentHealth.grid(row=0, column=0)
                pokemonHealth = Label(self.__opponentHealth, image=self.__sharpedoHealth75)
                pokemonHealth.grid()
            else:
                pass
        else:pass

        if HPList[0] <= 0 and HPList[1] <= 0 and HPList[2] <= 0 and HPList[3] <= 0 and HPList[4] <= 0 and \
            HPList[5] <= 0:
            sound.PlaySound("Loser", sound.SND_FILENAME)
            print("You Were Defeated by PyCharmer Ribic.")
            winner = "Haris"
            self.displayWinner(winner)

        elif HPList[6] <= 0 and HPList[7] <= 0 and HPList[8] <= 0 and HPList[9] <= 0 and HPList[10] <= 0 and \
            HPList[11] <= 0:
            sound.PlaySound("Winner", sound.SND_FILENAME)
            print("You Defeated PyCharmer Ribic.")
            winner = "Player"
            self.displayWinner(winner)

        else:
            pass

        if player.getHP() <= 0:
            self.__playerPkmn.destroy()
            self.__playerPkmn = Frame(self)
            self.__playerPkmn.grid(row=1, column=0)
            trainer = Label(self.__playerPkmn, image=self.__trainer)
            trainer.grid()

            self.__playerHealth.destroy()
            self.__playerHealth = Frame(self)
            self.__playerHealth.grid(row=1, column=1)
            playerPokeballs = Label(self.__playerHealth, image=self.__playerPokeballs)
            playerPokeballs.grid()

        if AI.getHP() <= 0:
            self.__opponentPkmn.destroy()
            self.__opponentPkmn = Frame(self)
            self.__opponentPkmn.grid(row=0, column=1)

            haris = Label(self.__opponentPkmn, image=self.__haris)
            haris.grid()

        print(HPList)

        self.startingPoint(AI, HPList, AIHP, player, playerHP)
    

    #Displays the winner of the game and quits out of the game
    def displayWinner(self, winner):
        if winner == "Haris":
            showinfo(title= "You lost", message="You were defeated by PyCharmer Ribic.", parent = self.master.destroy())
        else:
            showinfo(title= "You won!", message="You defeated PyCharmer Ribic!", parent = self.master.destroy())


#Narrative: Sets AI, Player, AIHP, and PlayerHP as dummy values, sets all of pokemon HPs, and begins the game loop
def main():
    #Establishes Dummy Values for AI, player, AIHP, and playerHP, which will
    #be overwritten later
    AI = "Dummy"
    player = "Dummy"
    AIHP = 0
    playerHP = 0

    #Establishes HP Values for each Pokemon, that is one point higher than their
    #maximum HP, in order for the program to recognize when it is their first
    #turn on the field
    flygonHP = 156
    roseradeHP = 136
    togekissHP = 161
    bulbasaurHP = 121
    pikachuHP = 111
    tyranitarHP = 176
    sharpedoHP = 146
    magnezoneHP = 146
    banetteHP = 140
    poliwrathHP = 166
    noivernHP = 161
    aurorusHP = 199

    #Puts all HP Values into a list for easy calling
    HPList = [flygonHP, roseradeHP, togekissHP, bulbasaurHP,
              pikachuHP, tyranitarHP, sharpedoHP, magnezoneHP,
              banetteHP, poliwrathHP, noivernHP, aurorusHP]

    #Let The Games, BEGIN!
    PokemonGUI(AI, HPList, AIHP, player, playerHP).mainloop()


main()