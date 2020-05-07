import os
path = os.path.dirname(__file__)
os.chdir(path)

GUIs = []
class Gui:
    def __init__(self, gameHandler, name):
        self.gameHandler = gameHandler
        self.name = name
        self.pygame = gameHandler.pygame
        self.display = gameHandler.display
        self.showGUI = False 
        self.pressed = True
        self.arrowPos = 3.25

        GUIs.append(self)
        print(GUIs)

        self.arrow = self.pygame.image.load("graphics/gui/arrow.png")
        self.gui_top = self.pygame.image.load("graphics/gui/top.png")
        self.gui_left = self.pygame.image.load("graphics/gui/left.png")
        self.gui_bottom = self.pygame.image.load("graphics/gui/bottom.png")
        self.gui_right = self.pygame.image.load("graphics/gui/right.png")
        self.gui_top_left = self.pygame.image.load("graphics/gui/top-left.png")
        self.gui_top_right = self.pygame.image.load("graphics/gui/top-right.png")
        self.gui_bottom_left = self.pygame.image.load("graphics/gui/bottom-left.png")
        self.gui_bottom_right = self.pygame.image.load("graphics/gui/bottom-right.png")

        self.font = self.pygame.font.Font("fonts/PIXELADE.TTF", 24)

    def tick(self):
        pass
                
    def getGUI(self, name):
        for gui in GUIs:
            if (gui.name == name):
                return gui

    def drawGUI(self, xOffset, yOffset, width, height):
        self.pygame.draw.rect(self.display, (255, 255, 255), (xOffset, yOffset, width, height))

        for y in range(0, 3):
            for x in range(0, 3):
                if (x == 0 and y == 0):
                    self.display.blit(self.gui_top_left, (x + xOffset, y + yOffset))
                elif (x == 2 and y == 0):
                    self.display.blit(self.gui_top_right, (width + xOffset, y + yOffset))
                elif (x == 0 and y == 2):
                    self.display.blit(self.gui_bottom_left, (x + xOffset, height + yOffset - 6))
                elif (x == 2 and y == 2):
                    self.display.blit(self.gui_bottom_right, (width + xOffset, height + yOffset - 6))
                elif (x == 1 and y == 0):
                    self.display.blit(self.guiTop, (x * 6 + xOffset, y + yOffset))
                elif (x == 1 and y == 2):
                    self.display.blit(self.guiBottom, (x * 6 + xOffset, height + yOffset - 6))
                elif (x == 0 and y == 1):
                    self.display.blit(self.guiLeft, (x + xOffset, yOffset + 6))
                elif (x == 2 and y == 1):
                    self.display.blit(self.guiRight, (width + xOffset, yOffset + 6))

    def scaleGUI(self):
        self.guiTop = self.gameHandler.pygame.transform.scale(self.gui_top, (self.width, 6))
        self.guiBottom = self.pygame.transform.scale(self.gui_bottom, (self.width, 6))
        self.guiLeft = self.pygame.transform.scale(self.gui_left, (6, self.height - 6))
        self.guiRight = self.pygame.transform.scale(self.gui_right, (6, self.height - 6))

