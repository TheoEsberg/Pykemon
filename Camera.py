class Camera:
    def __init__(self, gameHandler):
        self.gameHandler = gameHandler
        self.xOffset = 0
        self.yOffset = 0

    def centerCamera(self, entity):
        if ((self.gameHandler.currentMap.width * self.gameHandler.currentMap.tilewidth) > self.gameHandler.displayWidth):
            self.xOffset = max(0, min(self.gameHandler.currentMap.width * self.gameHandler.currentMap.tilewidth - self.gameHandler.displayWidth, entity.x + (entity.width/2) - (self.gameHandler.displayWidth/2)))
        else:
            self.xOffset = (self.gameHandler.currentMap.width * self.gameHandler.currentMap.tilewidth) / 2 - (self.gameHandler.displayWidth / 2)
        
        if ((self.gameHandler.currentMap.height * self.gameHandler.currentMap.tileheight) > self.gameHandler.displayHeight):
            self.yOffset = max(0, min(self.gameHandler.currentMap.height * self.gameHandler.currentMap.tileheight - self.gameHandler.displayHeight ,entity.y + (entity.height/2) - (self.gameHandler.displayHeight/2)))
        else: 
            self.yOffset = (self.gameHandler.currentMap.height * self.gameHandler.currentMap.tileheight) / 2 - (self.gameHandler.displayHeight / 2)

    