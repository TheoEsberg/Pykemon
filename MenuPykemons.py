import GUI

class MenuPykemons(GUI.Gui):
    def __init__(self, gameHandler):
        super().__init__(gameHandler, "pykemons")
        self.width = 160
        self.height = 170
        self.scaleGUI()

        self.xOffset = (self.gameHandler.displayWidth - self.width - 6) - 24
        self.yOffset = (self.gameHandler.displayHeight / 2 - self.height / 2)

        #   All pokemons texts
        self.pokemon1 = self.font.render("None", True, (0, 0, 0))
        self.pokemon2 = self.font.render("None", True, (0, 0, 0))
        self.pokemon3 = self.font.render("None", True, (0, 0, 0))
        self.pokemon4 = self.font.render("None", True, (0, 0, 0))
        self.pokemon5 = self.font.render("None", True, (0, 0, 0))
        self.pokemon6 = self.font.render("None", True, (0, 0, 0))

        #   Change the pokemon text if there is an avalible pokemon in the caughtPokemons list inside the gamehandler
        if (len(self.gameHandler.caughtPokemons) == 1):
            self.pokemon1 = self.font.render(self.gameHandler.caughtPokemons[0].name, True, (0, 0, 0))
        elif (len(self.gameHandler.caughtPokemons) == 2):
            self.pokemon2 = self.font.render(self.gameHandler.caughtPokemons[1].name, True, (0, 0, 0))
        elif (len(self.gameHandler.caughtPokemons) == 3):
            self.pokemon3 = self.font.render(self.gameHandler.caughtPokemons[2].name, True, (0, 0, 0))
        elif (len(self.gameHandler.caughtPokemons) == 4):
            self.pokemon4 = self.font.render(self.gameHandler.caughtPokemons[3].name, True, (0, 0, 0))
        elif (len(self.gameHandler.caughtPokemons) == 5):
            self.pokemon5 = self.font.render(self.gameHandler.caughtPokemons[4].name, True, (0, 0, 0))
        elif (len(self.gameHandler.caughtPokemons) == 6):
            self.pokemon6 = self.font.render(self.gameHandler.caughtPokemons[5].name, True, (0, 0, 0))


    def tick(self):
        self.inputs()
        #   Rendering the GUI
        if (self.showGUI == True):
            self.drawGUI(self.xOffset, self.yOffset, self.width, self.height)
            self.display.blit(self.pokemon1, (self.xOffset + (6 * 8), self.yOffset + (6 * 2)))
            self.display.blit(self.pokemon2, (self.xOffset + (6 * 8), self.yOffset + (6 * 6)))
            self.display.blit(self.pokemon3, (self.xOffset + (6 * 8), self.yOffset + (6 * 10)))
            self.display.blit(self.pokemon4, (self.xOffset + (6 * 8), self.yOffset + (6 * 14)))
            self.display.blit(self.pokemon5, (self.xOffset + (6 * 8), self.yOffset + (6 * 18)))
            self.display.blit(self.pokemon6, (self.xOffset + (6 * 8), self.yOffset + (6 * 22)))
            self.display.blit(self.arrow, (self.xOffset + (6 * 4), self.yOffset + (6 * self.arrowPos)))

    def updatePokemonList(self):
        #   Update the list of pokemons if you get a new pokemon ingame
        if (len(self.gameHandler.caughtPokemons) == 1):
            self.pokemon1 = self.font.render(self.gameHandler.caughtPokemons[0].name, True, (0, 0, 0))
        elif (len(self.gameHandler.caughtPokemons) == 2):
            self.pokemon2 = self.font.render(self.gameHandler.caughtPokemons[1].name, True, (0, 0, 0))
        elif (len(self.gameHandler.caughtPokemons) == 3):
            self.pokemon3 = self.font.render(self.gameHandler.caughtPokemons[2].name, True, (0, 0, 0))
        elif (len(self.gameHandler.caughtPokemons) == 4):
            self.pokemon4 = self.font.render(self.gameHandler.caughtPokemons[3].name, True, (0, 0, 0))
        elif (len(self.gameHandler.caughtPokemons) == 5):
            self.pokemon5 = self.font.render(self.gameHandler.caughtPokemons[4].name, True, (0, 0, 0))
        elif (len(self.gameHandler.caughtPokemons) == 6):
            self.pokemon6 = self.font.render(self.gameHandler.caughtPokemons[5].name, True, (0, 0, 0))

    def inputs(self):
        #   Get the inputs, move the arrow, you probebly get it by now...
        keys = self.pygame.key.get_pressed()
        if (self.showGUI == True):
            if (keys[self.pygame.K_DOWN]):
                if (self.pressed == False):
                    self.pressed = True
                    if (self.arrowPos + 4 > 3.25 + (4 * 5)):
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
                if (self.pressed == False):
                    self.pressed = True
                    for i in range(len(self.gameHandler.caughtPokemons)):
                        if (self.arrowPos == 3.25 + 4 * i):
                            self.gameHandler.activePokemon = self.gameHandler.caughtPokemons[i]
                            print(self.gameHandler.activePokemon.name)
                    self.showGUI = False

            #   Exit menu on escape
            elif (keys[self.pygame.K_ESCAPE]):
                self.showGUI = False
               
            else:
                self.pressed = False