class SpriteSheets:
    def __init__(self, gameHandler):
        self.gameHandler = gameHandler
        
    def GetSprites(self, spriteSheet, spriteWidth, spriteHeight, start, stop):
        sprites = []
        for i in range(start - 1, stop):
            sprite = spriteSheet.subsurface((i * spriteWidth, 0, spriteWidth, spriteHeight))
            sprites.append(sprite)
        return sprites

    def GetPokeSprites(self, spriteSheet, spriteWidth, spriteHeight, x, y):
        sprites = []
        for i in range(2):
            sprite = spriteSheet.subsurface((((x-1) * spriteWidth), ((y-1) * spriteHeight) + (i * spriteHeight), spriteWidth, spriteHeight))
            sprites.append(sprite)
        return sprites

       