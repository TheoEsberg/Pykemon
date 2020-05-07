import GUI
import random

class battle():
    def __init__(self, gameHandler):
        self.gameHandler = gameHandler
        self.gameHandler.battle = self

        self.leftGUI = GUI.Gui(gameHandler, "leftBattleGUI")
        self.leftGUI.width = int(self.gameHandler.displayWidth / 3) * 2
        self.leftGUI.height = int(self.gameHandler.displayHeight / 5)
        self.leftGUI.xOffset = 0
        self.leftGUI.yOffset = self.gameHandler.displayHeight - int(self.gameHandler.displayHeight / 5)
        self.leftGUI.scaleGUI()

        self.rightGUI = GUI.Gui(gameHandler, "rightBattleGUI")
        self.rightGUI.width = self.gameHandler.displayWidth - self.leftGUI.width - 12
        self.rightGUI.height = int(self.gameHandler.displayHeight / 5)
        self.rightGUI.xOffset = self.leftGUI.width + 6
        self.rightGUI.yOffset = self.gameHandler.displayHeight - int(self.gameHandler.displayHeight / 5)
        self.rightGUI.scaleGUI()

        self.backgroundOG = self.gameHandler.pygame.image.load("graphics/gui/battleGUI/battle_bg.png")
        self.background = self.gameHandler.pygame.transform.scale(self.backgroundOG, (self.gameHandler.displayWidth, int(self.gameHandler.displayHeight / 5) * 4))

    def tick(self):
        self.gameHandler.display.blit(self.background, (0, 0))
        self.leftGUI.drawGUI(self.leftGUI.xOffset, self.leftGUI.yOffset, self.leftGUI.width, self.leftGUI.height)
        self.rightGUI.drawGUI(self.rightGUI.xOffset, self.rightGUI.yOffset, self.rightGUI.width, self.rightGUI.height)

    def initBattle(self):
        enemy = self.gameHandler.pokemons[int(random.randint(0, len(self.gameHandler.pokemons) - 1))]
        enemy.allowTick = True
        enemy.tick()
        print(enemy.name)
        print(enemy.hp)