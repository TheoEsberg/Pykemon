import GUI

class Menu(GUI.Gui):
    def __init__(self, gameHandler):
        super().__init__(gameHandler, "menu")
        self.width = 160
        self.height = 100
        self.scaleGUI()

        self.xOffset = (self.gameHandler.displayWidth - self.width - 6) - 24
        self.yOffset = (self.gameHandler.displayHeight / 2 - self.height / 2)

        #   This is the gui texts
        self.guiTxt = self.font.render("Inventory", True, (0, 0, 0))
        self.pykemonsTxt = self.font.render("Pykemons", True, (0, 0, 0))
        self.exitTxt = self.font.render("Exit", True, (0, 0, 0))

    def tick(self):
        self.inputs()
        #   Render the gui
        if (self.showGUI == True):
            self.drawGUI(self.xOffset, self.yOffset, self.width, self.height)
            self.display.blit(self.guiTxt, (self.xOffset + (6 * 8), self.yOffset + (6 * 2)))
            self.display.blit(self.pykemonsTxt, (self.xOffset + (6 * 8), self.yOffset + (6 * 6)))
            self.display.blit(self.exitTxt, (self.xOffset + (6 * 8), self.yOffset + (6 * 10)))
            self.display.blit(self.arrow, (self.xOffset + (6 * 4), self.yOffset + (6 * self.arrowPos)))

    def inputs(self):
        #   Getting the inputs
        keys = self.pygame.key.get_pressed()
        #   Open the gui by pressing the buttin "i"
        if (keys[self.pygame.K_i]):
            if (self.pressed == False):
                self.pressed = True
                self.showGUI = not self.showGUI
        elif (self.showGUI == True):
            #   Move the arrow with up and down
            if (keys[self.pygame.K_DOWN]):
                if (self.pressed == False):
                    self.pressed = True
                    if (self.arrowPos + 4 > 11.25):
                        return
                    else:
                        self.arrowPos += 4
            elif (keys[self.pygame.K_UP]):
                if (self.pressed == False):
                    self.pressed = True
                    if (self.arrowPos - 4 < 3.25):
                        return
                    else:
                        self.arrowPos -= 4
            elif (keys[self.pygame.K_RETURN]):
                #   Going to correct menu depending on arrow position
                if (self.pressed == False):
                    self.pressed = True
                    if (self.arrowPos == 3.25):
                        print("GO TO INVENTORY")
                    elif (self.arrowPos == 7.25):
                        self.getGUI("pykemons").showGUI = True
                        self.getGUI("pykemons").updatePokemonList()
                        print("GO TO PYKEMONS")
                    elif (self.arrowPos == 11.25):
                        print("GO TO EXIT")
                    self.showGUI = False
            else:
                self.pressed = False
        else:
            self.pressed = False

    

