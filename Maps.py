from pytmx import load_pygame, TiledTileLayer
import pytmx, os
path = os.path.dirname(__file__)
os.chdir(path)

class Maps:
    def __init__(self, gameHandler):
        self.gameHandler = gameHandler
        self.screenWidth = gameHandler.displayWidth
        self.screenHeight = gameHandler.displayHeight
        self.screen = gameHandler.display

    def render(self):
        #   Rendering the map by going through each layer and blitting the correct tile on the correct position.
        #   This also makes sure to not blitting images outside of the camera to save on performance
        self.ti = self.gameHandler.currentMap.get_tile_image_by_gid
        xStart = max(0, self.gameHandler.camera.xOffset / self.gameHandler.currentMap.tilewidth)
        xEnd = min(self.gameHandler.currentMap.width, (self.gameHandler.camera.xOffset + self.gameHandler.displayWidth) / self.gameHandler.currentMap.tilewidth + 1)
        yStart = max(0, self.gameHandler.camera.yOffset / self.gameHandler.currentMap.tileheight)
        yEnd = min(self.gameHandler.currentMap.height, (self.gameHandler.camera.yOffset + self.gameHandler.displayHeight) / self.gameHandler.currentMap.tileheight + 1)
        for i in range(len(self.gameHandler.currentMap.layers) - 1):
            for x in range(int(xStart), int(xEnd)):
                for y in range(int(yStart), int(yEnd)):
                    tile = self.gameHandler.currentMap.get_tile_image(x, y, i)
                    if (tile):
                        self.screen.blit(tile, (x * self.gameHandler.currentMap.tilewidth - self.gameHandler.camera.xOffset,
                                                y * self.gameHandler.currentMap.tileheight - self.gameHandler.camera.yOffset))
