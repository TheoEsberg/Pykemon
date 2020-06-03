import GUI
import random

class battle(GUI.Gui):
    def __init__(self, gameHandler):
        super().__init__(gameHandler, "Battle")
        self.gameHandler = gameHandler
        self.gameHandler.battle = self
        self.enemy = None
        self.arrowPos = 1
        self.menuStage = 0
        self.goFirst = True
        self.readyToAttack = True

        #   Left Gui Box
        self.leftGUI = GUI.Gui(gameHandler, "leftBattleGUI")
        self.leftGUI.width = int(self.gameHandler.displayWidth / 3) * 2
        self.leftGUI.height = int(self.gameHandler.displayHeight / 5)
        self.leftGUI.xOffset = 0
        self.leftGUI.yOffset = self.gameHandler.displayHeight - int(self.gameHandler.displayHeight / 5)
        self.leftGUI.scaleGUI()

        #   Right Gui Box 
        self.rightGUI = GUI.Gui(gameHandler, "rightBattleGUI")
        self.rightGUI.width = self.gameHandler.displayWidth - self.leftGUI.width - 12
        self.rightGUI.height = int(self.gameHandler.displayHeight / 5)
        self.rightGUI.xOffset = self.leftGUI.width + 6
        self.rightGUI.yOffset = self.gameHandler.displayHeight - int(self.gameHandler.displayHeight / 5)
        self.rightGUI.scaleGUI()

        #   Right Gui Box Text
        self.attack = self.font.render("Attack", True, (0, 0, 0))
        self.pokemons = self.font.render("Pokemons", True, (0, 0, 0))
        self.inventory = self.font.render("Inventory", True, (0, 0, 0))
        self.run = self.font.render("Run", True, (0, 0, 0))


        #   Battle Background
        self.backgroundOG = self.gameHandler.pygame.image.load("graphics/gui/battleGUI/battle_bg.png")
        self.background = self.gameHandler.pygame.transform.scale(self.backgroundOG, (self.gameHandler.displayWidth, int(self.gameHandler.displayHeight / 5) * 4))


    def tick(self):
        #   Rendering the background and the two guis 
        self.gameHandler.display.blit(self.background, (0, 0))
        self.leftGUI.drawGUI(self.leftGUI.xOffset, self.leftGUI.yOffset, self.leftGUI.width, self.leftGUI.height)
        self.rightGUI.drawGUI(self.rightGUI.xOffset, self.rightGUI.yOffset, self.rightGUI.width, self.rightGUI.height)

        #   This is the gui text system wich displays text depending on what is happening in the battle
        if (self.menuStage == 0):
            self.display.blit(self.wild, ((self.leftGUI.width / 2) - (self.wild.get_width() / 2), self.gameHandler.displayHeight - int((self.gameHandler.displayHeight / 5) / 2) - self.wild.get_height() / 2))
        elif (self.menuStage == 1):
            self.display.blit(self.whatToDo, ((self.leftGUI.width / 2) - (self.whatToDo.get_width() / 2), self.gameHandler.displayHeight - int((self.gameHandler.displayHeight / 5) / 2) - self.whatToDo.get_height() / 2))
        elif (self.menuStage == 2):
            self.display.blit(self.attack, (self.leftGUI.width + self.rightGUI.width / 6, self.gameHandler.displayHeight - int(self.gameHandler.displayHeight / 5) + self.attack.get_height() * 1.5))
            self.display.blit(self.pokemons, (self.gameHandler.displayWidth - self.run.get_width() - self.rightGUI.width / 4, self.gameHandler.displayHeight - int(self.gameHandler.displayHeight / 5) + self.pokemons.get_height() * 1.5))
            self.display.blit(self.inventory, (self.leftGUI.width + self.rightGUI.width / 6, self.gameHandler.displayHeight - self.inventory.get_height() * 2))
            self.display.blit(self.run, (self.gameHandler.displayWidth - self.run.get_width() - self.rightGUI.width / 4, self.gameHandler.displayHeight - self.run.get_height() * 2))
            self.drawArrow()
        elif (self.menuStage == 3):
            self.display.blit(self.move1, (self.leftGUI.width + self.rightGUI.width / 6, self.gameHandler.displayHeight - int(self.gameHandler.displayHeight / 5) + self.attack.get_height() * 1.5))
            self.display.blit(self.move2, (self.gameHandler.displayWidth - self.run.get_width() - self.rightGUI.width / 4, self.gameHandler.displayHeight - int(self.gameHandler.displayHeight / 5) + self.pokemons.get_height() * 1.5))
            self.display.blit(self.move3, (self.leftGUI.width + self.rightGUI.width / 6, self.gameHandler.displayHeight - self.inventory.get_height() * 2))
            self.display.blit(self.move4, (self.gameHandler.displayWidth - self.run.get_width() - self.rightGUI.width / 4, self.gameHandler.displayHeight - self.run.get_height() * 2))
            self.drawArrow()
        #   Here is the attack applyed to the two entites, this is depending on who has the highest speed stat
        elif (self.menuStage == 4):
            if (self.goFirst == True and self.BattlePokemon.hp > 0):
                self.display.blit(self.myMoveUsed, ((self.leftGUI.width / 2) - (self.myMoveUsed.get_width() / 2), self.gameHandler.displayHeight - int((self.gameHandler.displayHeight / 5) / 2) - self.myMoveUsed.get_height() / 2))
                if (self.readyToAttack == True):
                    self.readyToAttack = False
                    self.enemy.hp -= self.BattlePokemon.attack
                    print(str(self.enemy.name) + " " + str(self.enemy.hp))
            else:
                if (self.enemy.hp > 0):
                    self.display.blit(self.enemyMoveUsed, ((self.leftGUI.width / 2) - (self.enemyMoveUsed.get_width() / 2), self.gameHandler.displayHeight - int((self.gameHandler.displayHeight / 5) / 2) - self.enemyMoveUsed.get_height() / 2))
                    if (self.readyToAttack == True):
                        self.readyToAttack = False
                        self.BattlePokemon.hp -= self.enemy.attack
                        print(str(self.BattlePokemon.name) + " " + str(self.BattlePokemon.hp))
        elif (self.menuStage == 5):
            if (self.goFirst == False and self.BattlePokemon.hp > 0):
                self.display.blit(self.myMoveUsed, ((self.leftGUI.width / 2) - (self.myMoveUsed.get_width() / 2), self.gameHandler.displayHeight - int((self.gameHandler.displayHeight / 5) / 2) - self.myMoveUsed.get_height() / 2))
                if (self.readyToAttack == True):
                    self.readyToAttack = False
                    self.enemy.hp -= self.BattlePokemon.attack
                    print(str(self.enemy.name) + " " + str(self.enemy.hp))
            else:
                if (self.enemy.hp > 0 and self.BattlePokemon.hp > 0):
                    self.display.blit(self.enemyMoveUsed, ((self.leftGUI.width / 2) - (self.enemyMoveUsed.get_width() / 2), self.gameHandler.displayHeight - int((self.gameHandler.displayHeight / 5) / 2) - self.enemyMoveUsed.get_height() / 2))
                    if (self.readyToAttack == True):
                        self.readyToAttack = False
                        self.BattlePokemon.hp -= self.enemy.attack
                        print(str(self.BattlePokemon.name) + " " + str(self.BattlePokemon.hp))
                else:
                    self.menuStage = 6
        elif (self.menuStage == 6):
            if (self.BattlePokemon.hp <= 0):
                self.display.blit(self.myDeadMsg, ((self.leftGUI.width / 2) - (self.myDeadMsg.get_width() / 2), self.gameHandler.displayHeight - int((self.gameHandler.displayHeight / 5) / 2) - self.myDeadMsg.get_height() / 2))
            elif (self.enemy.hp <= 0):
                self.display.blit(self.enemyDeadMsg, ((self.leftGUI.width / 2) - (self.enemyDeadMsg.get_width() / 2), self.gameHandler.displayHeight - int((self.gameHandler.displayHeight / 5) / 2) - self.enemyDeadMsg.get_height() / 2))


        #   Get the inputs and draw the entites
        self.inputs()
        if (self.enemy != None):
            self.enemy.tick()
            self.BattlePokemon.tick()

    #   This is a input handler that get the pressed key
    def inputs(self):
        keys = self.pygame.key.get_pressed()
        #   Here I move the arrow
        if (keys[self.pygame.K_LEFT]):
            if (self.pressed == False):
                self.pressed = True
                if (self.arrowPos == 2):
                    self.arrowPos = 1
                elif (self.arrowPos == 4):
                    self.arrowPos = 3
        elif (keys[self.pygame.K_RIGHT]):
            if (self.pressed == False):
                self.pressed = True
                if (self.arrowPos == 1):
                    self.arrowPos = 2
                elif (self.arrowPos == 3):
                    self.arrowPos = 4
        elif (keys[self.pygame.K_UP]):
            if (self.pressed == False):
                self.pressed = True
                if (self.arrowPos == 3):
                    self.arrowPos = 1
                elif (self.arrowPos == 4):
                    self.arrowPos = 2
        elif (keys[self.pygame.K_DOWN]):
            if (self.pressed == False):
                self.pressed = True
                if (self.arrowPos == 1):
                    self.arrowPos = 3
                elif (self.arrowPos == 2):
                    self.arrowPos = 4

        #   Checking for the button "enter" and decide what to do depending on arrow position
        elif (keys[self.pygame.K_RETURN]):
            if (self.pressed == False):
                self.pressed = True
                
                #   This is the fighting options in the battle menu   
                if (self.menuStage == 2 and self.arrowPos == 1):
                    self.menuStage = 3
                elif (self.menuStage == 3):
                    if (self.arrowPos == 1):
                        self.myMoveUsed = self.font.render(str(self.BattlePokemon.name + " used " + str(self.BattlePokemon.moves[0])), True, (0, 0, 0))
                    elif (self.arrowPos == 2):
                        self.myMoveUsed = self.font.render(str(self.BattlePokemon.name + " used " + str(self.BattlePokemon.moves[1])), True, (0, 0, 0))
                    elif (self.arrowPos == 3):
                        self.myMoveUsed = self.font.render(str(self.BattlePokemon.name + " used " + str(self.BattlePokemon.moves[2])), True, (0, 0, 0))
                    elif (self.arrowPos == 4):
                        self.myMoveUsed = self.font.render(str(self.BattlePokemon.name + " used " + str(self.BattlePokemon.moves[3])), True, (0, 0, 0))
                    self.enemyMoveUsed = self.font.render(str(self.enemy.name + " used " + str(self.enemy.moves[random.randint(0, 3)])), True, (0, 0, 0))
                    self.menuStage = 4
                    self.readyToAttack = True
                    self.arrowPos = 1
                elif(self.menuStage == 4):
                    self.readyToAttack = True
                    self.menuStage = 5
                elif (self.menuStage == 5 and self.BattlePokemon.hp > 0 and self.enemy.hp > 0):
                    self.menuStage = 2
                elif (self.menuStage == 6):
                    self.enemy.allowTick = False
                    self.enemy.battleMode = False
                    self.BattlePokemon.allowTick = False
                    self.BattlePokemon.battleMode = False
                    self.gameHandler.ReloadPokemons()
                    self.menuStage = 0
                    self.gameHandler.pokemonFight = False
                else:
                    if (self.menuStage != 2):
                        print(self.menuStage)
                        self.menuStage += 1

                #   The run button to end the battle
                if (self.menuStage == 2 and self.arrowPos == 4):
                    self.enemy.allowTick = False
                    self.enemy.battleMode = False
                    self.BattlePokemon.allowTick = False
                    self.BattlePokemon.battleMode = False
                    self.gameHandler.ReloadPokemons()
                    self.menuStage = 0
                    self.arrowPos = 1
                    self.gameHandler.pokemonFight = False
        else: 
            self.pressed = False

    def drawArrow(self):
        #   Drawing the arrow on a specific point 
        if (self.arrowPos == 1):
            self.display.blit(self.arrow, (self.leftGUI.width + self.rightGUI.width / 6 - 12, self.gameHandler.displayHeight - int(self.gameHandler.displayHeight / 5) + self.attack.get_height() * 1.5 + 6))
        elif (self.arrowPos == 2):
             self.display.blit(self.arrow, (self.gameHandler.displayWidth - self.run.get_width() - self.rightGUI.width / 4 - 12, self.gameHandler.displayHeight - int(self.gameHandler.displayHeight / 5) + self.pokemons.get_height() * 1.5 + 6))
        elif (self.arrowPos == 3):
            self.display.blit(self.arrow, (self.leftGUI.width + self.rightGUI.width / 6 - 12, self.gameHandler.displayHeight - self.inventory.get_height() * 2 + 6))
        elif (self.arrowPos == 4):
            self.display.blit(self.arrow, (self.gameHandler.displayWidth - self.run.get_width() - self.rightGUI.width / 4 - 12, self.gameHandler.displayHeight - self.run.get_height() * 2 + 6))
    def initBattle(self):
        #   Initialize the Enemy
        self.enemy = self.gameHandler.pokemons[int(random.randint(0, len(self.gameHandler.pokemons) - 1))]
        self.enemy.allowTick = True
        self.enemy.battleMode = True
        self.enemy.x = self.gameHandler.displayWidth - (self.gameHandler.displayWidth / 4) - (self.enemy.ImageBattle.get_width() / 2)
        self.enemy.y = (self.gameHandler.displayHeight / 3)

        #   Initialize your Pokemon
        self.BattlePokemon = self.gameHandler.activePokemon
        self.BattlePokemon.allowTick = True
        self.BattlePokemon.battleMode = True
        self.BattlePokemon.x = (self.gameHandler.displayWidth / 4) - (self.enemy.ImageBattle.get_width() / 3)
        self.BattlePokemon.y = self.gameHandler.displayHeight - (self.gameHandler.displayHeight / 3)

        #   Decide who will attack first depending on the speed of the pokemons
        if (self.enemy.speed > self.BattlePokemon.speed):
            self.goFirst = False
        else:
            self.goFirst = True

        #   The text for seeing a pokemon
        self.wild = self.font.render("A Wild " + str(self.enemy.name) + " Has Appeared", True, (0, 0, 0))
        self.whatToDo = self.font.render("What will " + str(self.BattlePokemon.name) + " Do?", True, (0, 0, 0))

        #   The attacks aka moves text
        self.move1 = self.font.render(str(self.BattlePokemon.moves[0]), True, (0, 0, 0))
        self.move2 = self.font.render(str(self.BattlePokemon.moves[1]), True, (0, 0, 0))
        self.move3 = self.font.render(str(self.BattlePokemon.moves[2]), True, (0, 0, 0))
        self.move4 = self.font.render(str(self.BattlePokemon.moves[3]), True, (0, 0, 0))

        #   The fainted message
        self.myDeadMsg = self.font.render(str(self.BattlePokemon.name + " has fainted."), True, (0, 0, 0))
        self.enemyDeadMsg = self.font.render(str(self.enemy.name + " has fainted."), True, (0, 0, 0))

        print(self.enemy.name)
        print(self.enemy.hp)