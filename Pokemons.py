import os
import Entity, Player, SpriteSheets, Timer

path = os.path.dirname(__file__)
os.chdir(path)

class Pokemons(Entity.Entity):
    def __init__(self, gameHandler, name, type, hp, attack, defence, speed, moves, level, xp):
        super().__init__(0, 0, 32, 32, 0, gameHandler)
        self.gameHandler = gameHandler
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.moves = moves
        self.level = level 
        self.xp = xp
        self.battleMode = False

        #   Pokemons
        self.image = self.gameHandler.pygame.image.load("graphics/pokemons/"+self.name+".gif")

        #   Pokemon animation
        self.spriteSheets = SpriteSheets.SpriteSheets(self.gameHandler)
        self.ImageUp = self.spriteSheets.GetPokeSprites(self.image, 32, 32, 1, 1)
        self.ImageDown = self.spriteSheets.GetPokeSprites(self.image, 32, 32, 1, 3)
        self.ImageLeft = self.spriteSheets.GetPokeSprites(self.image, 32, 32, 2, 1)
        self.ImageRight = self.spriteSheets.GetPokeSprites(self.image, 32, 32, 2, 3)
        self.ImageBattle = self.gameHandler.pygame.image.load("graphics/pokemons/Battle/"+self.name+".gif")
        self.currentAnim = self.ImageUp

        #   Timer
        self.timer = Timer.Timer(.125)
        self.timer.Start()
        self.steps = 0

    def renderPokemon(self):
        #   Render the pokemon depending on the latest steps from the player
        if (self.x + self.width <= self.gameHandler.recentSteps[1][0]):
            self.x += self.MoveSpeed
            self.currentAnim = self.ImageRight
        if(self.x >= self.gameHandler.recentSteps[1][0]):
            self.x -= self.MoveSpeed
            self.currentAnim = self.ImageLeft
        if (self.y + self.height <= self.gameHandler.recentSteps[1][1]):
            self.y += self.MoveSpeed
            self.currentAnim = self.ImageDown
        if (self.y >= self.gameHandler.recentSteps[1][1]):
            self.y -= self.MoveSpeed
            self.currentAnim = self.ImageUp
        
        self.gameHandler.display.blit(self.currentAnim[self.steps], (self.x - self.gameHandler.camera.xOffset, 
                                                                     self.y - self.gameHandler.camera.yOffset + 32))

    def tick(self):
        #   Deceding what to render dependin on in battle or not
        if (self.allowTick == False and self.battleMode == False):
            return

        if (self.battleMode == False):
            self.renderPokemon()
            self.timer.UpdateTimer()
            if (self.timer.Finished == True):
                self.timer.Start()
                self.countSteps()
        else: 
            self.gameHandler.display.blit(self.ImageBattle, (self.x - 16, self.y - 32))
   
    #   Animation steps handler
    def countSteps(self):
        if (self.steps + 1 >= 2):
            self.steps = 0
        else:
            self.steps += 1
