import GUI

class GetStarter(GUI.Gui):
    def __init__(self, gameHandler):
        super().__init__(gameHandler, "getStarter")

        self.stage = 0
        self.width = 485
        self.height = 85
        self.scaleGUI()

        self.xOffset = self.gameHandler.displayWidth / 2 - (self.width / 2)
        self.yOffset = self.gameHandler.displayHeight - self.height - 24
        
        self.dialoge0 = self.font.render("[Oak] Hello there Ash,", True, (0, 0, 0))
        self.dialoge1 = self.font.render("I am Professor Oak here in Pallet Town", True, (0, 0, 0))
        self.dialoge2 = self.font.render("As you may know, today is the day when", True, (0, 0, 0))
        self.dialoge3 = self.font.render("you can get your own Pokemon.", True, (0, 0, 0))
        self.dialoge4 = self.font.render("[Ash] I know and I'm so exited!", True, (0, 0, 0))
        self.dialoge5 = self.font.render("Wich ones are avalible?", True, (0, 0, 0))
        self.dialoge6 = self.font.render("[Oak] We have three different pokemons", True, (0, 0, 0))
        self.dialoge7 = self.font.render("avalible for you, but you can only choose one!", True, (0, 0, 0))
        self.dialoge8 = self.font.render("[Oak] First we have Snivy. Snivy is a", True, (0, 0, 0))
        self.dialoge9 = self.font.render("grass type and perfekt as an starter.", True, (0, 0, 0))
        self.dialoge10 = self.font.render("[Oak] Then we have Tepig. Tepig is an fire pokemon", True, (0, 0, 0))
        self.dialoge11 = self.font.render("so be carefull, he has an 'hot' temper ;)", True, (0, 0, 0))
        self.dialoge12 = self.font.render("[Oak] Last but not least we have Oshawott.", True, (0, 0, 0))
        self.dialoge13 = self.font.render("He is an water pokemon. Wich one will you choose?", True, (0, 0, 0))
        self.dialoge14 = self.font.render("You have already chosen your pokemon.", True, (0, 0, 0))
        self.dialoge15 = self.font.render("You should go out and try to catch some more Pokemons.", True, (0, 0, 0))

        self.choose1 = self.font.render("Snivy", True, (0, 0, 0))
        self.choose2 = self.font.render("Tepig", True, (0, 0, 0))
        self.choose3 = self.font.render("Oshawott", True, (0, 0, 0))
        self.arrowPos = self.xOffset - self.choose1.get_width() * 2 + 24
        self.arrowStartPos = self.xOffset - self.choose1.get_width() * 2 + 24


    def tick(self):
        self.inputs()
        if (self.gameHandler.getStarterActive == True and self.stage <= 7):
            self.drawGUI(self.xOffset, self.yOffset, self.width, self.height)
            if (self.stage == 0):
                self.display.blit(self.dialoge0, (self.xOffset + (self.width / 2) - self.dialoge0.get_width() / 2, self.yOffset + 16))
                self.display.blit(self.dialoge1, (self.xOffset + (self.width / 2) - self.dialoge1.get_width() / 2, self.yOffset + 48))
            elif (self.stage == 1):
                self.display.blit(self.dialoge2, (self.xOffset + (self.width / 2) - self.dialoge2.get_width() / 2, self.yOffset + 16))
                self.display.blit(self.dialoge3, (self.xOffset + (self.width / 2) - self.dialoge3.get_width() / 2, self.yOffset + 48))
            elif (self.stage == 2):
                self.display.blit(self.dialoge4, (self.xOffset + (self.width / 2) - self.dialoge4.get_width() / 2, self.yOffset + 16))
                self.display.blit(self.dialoge5, (self.xOffset + (self.width / 2) - self.dialoge5.get_width() / 2, self.yOffset + 48))
            elif (self.stage == 3):
                self.display.blit(self.dialoge6, (self.xOffset + (self.width / 2) - self.dialoge6.get_width() / 2, self.yOffset + 16))
                self.display.blit(self.dialoge7, (self.xOffset + (self.width / 2) - self.dialoge7.get_width() / 2, self.yOffset + 48))
            elif (self.stage == 4):
                self.display.blit(self.dialoge8, (self.xOffset + (self.width / 2) - self.dialoge8.get_width() / 2, self.yOffset + 16))
                self.display.blit(self.dialoge9, (self.xOffset + (self.width / 2) - self.dialoge9.get_width() / 2, self.yOffset + 48))
            elif (self.stage == 5):
                self.display.blit(self.dialoge10, (self.xOffset + (self.width / 2) - self.dialoge10.get_width() / 2, self.yOffset + 16))
                self.display.blit(self.dialoge11, (self.xOffset + (self.width / 2) - self.dialoge11.get_width() / 2, self.yOffset + 48))
            elif (self.stage == 6):
                self.display.blit(self.dialoge12, (self.xOffset + (self.width / 2) - self.dialoge12.get_width() / 2, self.yOffset + 16))
                self.display.blit(self.dialoge13, (self.xOffset + (self.width / 2) - self.dialoge13.get_width() / 2, self.yOffset + 48))
            elif (self.stage == 7):
                self.display.blit(self.choose1, (self.xOffset + (self.width / 4) - self.choose1.get_width() / 4, self.yOffset + 32))
                self.display.blit(self.choose2, (self.xOffset + (self.width / 2) - self.choose2.get_width() / 2, self.yOffset + 32))
                self.display.blit(self.choose3, (self.xOffset - (self.width / 4) + self.width - self.choose3.get_width() / 4, self.yOffset + 32))
                self.display.blit(self.arrow, (self.xOffset + self.arrowPos, self.yOffset + 40))
        elif (self.gameHandler.gotStarterPokemon == True and self.stage == 9):
            self.drawGUI(self.xOffset, self.yOffset, self.width, self.height)
            self.display.blit(self.dialoge14, (self.xOffset + (self.width / 2) - self.dialoge14.get_width() / 2, self.yOffset + 16))
            self.display.blit(self.dialoge15, (self.xOffset + (self.width / 2) - self.dialoge15.get_width() / 2, self.yOffset + 48))


    def inputs(self):
        keys = self.pygame.key.get_pressed()
        if (self.gameHandler.getStarterActive == True or self.gameHandler.gotStarterPokemon == True):
            if (keys[self.pygame.K_RETURN]):
                if (self.pressed == False):
                    self.pressed = True
                    if (self.stage == 7):
                        if (self.arrowPos == self.arrowStartPos):
                            self.gameHandler.GetNewPokemon(0, 0)
                            print("You choosed Snivy")
                        elif (self.arrowPos == self.arrowStartPos + 110):
                            self.gameHandler.GetNewPokemon(1, 0)
                            print("You choosed Tepig")
                        elif (self.arrowPos == self.arrowStartPos + 220):
                            self.gameHandler.GetNewPokemon(2, 0)
                            print("You choosed Othawott")
                        self.gameHandler.getStarterActive = False
                        self.stage += 1

                    if (self.gameHandler.gotStarterPokemon == True and self.stage != 8):
                        self.stage = 8
                    elif (self.stage != 7):
                        self.stage += 1
                    print(self.stage)

            elif(keys[self.pygame.K_LEFT]): 
                if (self.pressed == False and self.stage == 7 and self.arrowPos > self.arrowStartPos):
                    self.pressed = True
                    self.arrowPos -= 110
            elif(keys[self.pygame.K_RIGHT]):
                if (self.pressed == False and self.stage == 7 and self.arrowPos < self.arrowStartPos + 220):
                    self.pressed = True
                    self.arrowPos += 110
            else: 
                self.pressed = False
