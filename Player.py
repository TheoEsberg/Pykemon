from pytmx import load_pygame, TiledTileLayer
import pytmx, os, random
path = os.path.dirname(__file__)
os.chdir(path)

#   Import my classes
import Timer, Entity, Maps, SpriteSheets, Pokemons

#   Inherit from the Entity class
class Player(Entity.Entity):
    def __init__(self, x, y, width, height, layer, gameHandler):
        super().__init__(x, y, width, height, layer, gameHandler) 
        self.allowTick = True
        self.pressed = True

        #   Get the players sprite sheet
        self.spriteSheets = SpriteSheets.SpriteSheets(self.gameHandler)

        #   Loading all sprites from the sprite sheet to be used in animation
        pygame = gameHandler.pygame
        self.AshSheet = pygame.image.load("graphics/players/ash/Sprite(32x64).gif")
        self.ashLeft = self.spriteSheets.GetSprites(self.AshSheet, 32, 64, 4, 6)
        self.ashLeftIdle = self.spriteSheets.GetSprites(self.AshSheet, 32, 64, 4, 4)
        self.ashRight = self.spriteSheets.GetSprites(self.AshSheet, 32, 64, 10, 12)
        self.ashRightIdle = self.spriteSheets.GetSprites(self.AshSheet, 32, 64, 10, 10)
        self.ashUp = self.spriteSheets.GetSprites(self.AshSheet, 32, 64, 7, 9)
        self.ashUpIdle = self.spriteSheets.GetSprites(self.AshSheet, 32, 64, 7, 7)
        self.ashDown = self.spriteSheets.GetSprites(self.AshSheet, 32, 64, 1, 3)
        self.ashDownIdle = self.spriteSheets.GetSprites(self.AshSheet, 32, 64, 1, 1)
        self.currentAnim = self.ashDownIdle
        self.pokeball = pygame.image.load("graphics/items/pokeball.gif")

        #   Steps varables
        self.steps = 0
        self.countSteps()

        #   Animation variables
        #   Self.timer is for the speed of the animation
        self.timer = Timer.Timer(.125)
        self.timer.Start()
        self.looking = ""

        #   Get the width and height of the screen
        self.screenWidth = gameHandler.displayWidth
        self.screenHeight = gameHandler.displayHeight

        #   The maps variables
        self.maps = Maps.Maps(self.gameHandler)

        #   Set the players latest steps to be its current position
        for i in range(2):
            self.gameHandler.recentSteps.append([self.x, self.y])

    #   This is the tick function, works like a Update() in C#
    #   It's being updated each frame from main.py
    def tick(self):
        self.move()
        self.lastPos()
        self.running()
        self.renderPlayer()
        self.ThrowBall()
        self.gameHandler.camera.centerCamera(self)

        self.timer.UpdateTimer()
        if (self.timer.Finished == True):
            self.timer.Start()
            self.countSteps()

    #   Render the player on the screen
    def renderPlayer(self):
        self.display.blit(self.currentAnim[self.steps], (self.x - self.gameHandler.camera.xOffset, self.y - self.gameHandler.camera.yOffset))

    #   Update which step im currently on and add one each time this is being called
    def countSteps(self):
        if (self.steps + 1 >= len(self.currentAnim)):
            self.steps = 0
        else:
            self.steps += 1

    #   Lastpos is used so that the pokemon can follow my latest position, currently saves my 2 latest positions, saves each 32 pixels aka each tile
    def lastPos(self):
        if (self.gameHandler.recentSteps[0][0] - self.x >= 32):
            self.gameHandler.recentSteps.insert(0, [self.x, self.y])
            self.gameHandler.recentSteps.pop()
            self.moved = True
        elif (self.gameHandler.recentSteps[0][0] - self.x <= -32):
            self.gameHandler.recentSteps.insert(0, [self.x, self.y])
            self.gameHandler.recentSteps.pop()
            self.moved = True
        elif (self.gameHandler.recentSteps[0][1] - self.y <= -32):
            self.gameHandler.recentSteps.insert(0, [self.x, self.y])
            self.gameHandler.recentSteps.pop()
            self.moved = True
        elif (self.gameHandler.recentSteps[0][1] - self.y >= 32):
            self.gameHandler.recentSteps.insert(0, [self.x, self.y])
            self.gameHandler.recentSteps.pop()
            self.moved = True

    #   Just a simple running function when pressing SHIFT
    def running(self):
        keys = self.pygame.key.get_pressed()
        if keys[self.pygame.K_LSHIFT]:
            self.MoveSpeed = 4
            if (self.gameHandler.activePokemon != None):
                self.gameHandler.activePokemon.MoveSpeed = 4
        else:
            self.MoveSpeed = 2
            if (self.gameHandler.activePokemon != None):
                self.gameHandler.activePokemon.MoveSpeed = 2

    #   Movement function to move the player
    def move(self):
        #   Change the animation depending on current button pressed
        keys = self.pygame.key.get_pressed()
        if keys[self.pygame.K_a]:
            self.xVel = -self.MoveSpeed
            self.currentAnim = self.ashLeft
            self.looking = "left"
        elif keys[self.pygame.K_d]:
            self.xVel = self.MoveSpeed
            self.currentAnim = self.ashRight
            self.looking = "right"
        elif keys[self.pygame.K_w]:
            self.yVel = -self.MoveSpeed
            self.currentAnim = self.ashUp
            self.looking = "up"
        elif keys[self.pygame.K_s]:
            self.yVel = self.MoveSpeed
            self.currentAnim = self.ashDown
            self.looking = "down"
        else:
            self.steps = 0
            if (self.looking == "left"):
                self.currentAnim = self.ashLeftIdle
            elif (self.looking == "right"):
                self.currentAnim = self.ashRightIdle
            elif (self.looking == "up"):
                self.currentAnim = self.ashUpIdle
            else:
                self.currentAnim = self.ashDownIdle

        #   If it is not collideing then apply the movement
        if (self.collision() == False): 
            self.x += self.xVel
            self.y += self.yVel

        #   Reset the velocity to 0 so the player does not accelerate faster and faster each frame
        self.xVel = 0
        self.yVel = 0

    #   Transition (black fade, in and out)
    def Transition(self, fadeIn):
        self.transition = self.gameHandler.pygame.Surface((self.screenWidth, self.screenHeight))
        self.transition.fill((0, 0, 0))
        if (fadeIn == True):
            for alpha in range(0, 50):
                self.transition.set_alpha(alpha * 5.1)
                self.maps.render()
                self.display.blit(self.transition, (0, 0))
                self.pygame.display.update()
                self.pygame.time.delay(1)
        else:
            for alpha in range(0, 50):
                self.transition.set_alpha(255 - (alpha * 5.1))
                self.maps.render()
                self.renderPlayer()
                self.display.blit(self.transition, (0, 0))
                self.pygame.display.update()
                self.pygame.time.delay(1)
    #   Transition (white fade, in and out fast)
    def battleTransition(self):
        self.transition = self.gameHandler.pygame.Surface((self.screenWidth, self.screenHeight))
        self.transition.fill((255, 255, 255))
        for i in range(3):
            for alpha in range(0, 15):
                self.transition.set_alpha(alpha * 17)
                self.maps.render()
                self.display.blit(self.transition, (0, 0))
                self.pygame.display.update()
                self.pygame.time.delay(1)
            for alpha in range(0, 15):
                self.transition.set_alpha(255 - (alpha * 17))
                self.maps.render()
                self.renderPlayer()
                self.display.blit(self.transition, (0, 0))
                self.pygame.display.update()
                self.pygame.time.delay(1)

    #   ThrowBall is throwing your pokeball
    def ThrowBall(self):
        if (self.gameHandler.activePokemon != None):
            self.xBall = 0
            self.yBall = 0
            self.xSpeed = 2
            self.ballUp = True
            keys = self.pygame.key.get_pressed()
            if keys[self.pygame.K_r]:
                if(self.pressed == False):
                    self.pressed = True
                    if (self.gameHandler.activePokemon.allowTick == False):
                        #   Throw the ball in different directions
                        if (self.looking == "right"):
                            for i in range(64):
                                self.xBallOffset = 16
                                self.yBallOffset = 20
                                if (self.yBall < -10):
                                    self.ballUp = False
                                if (self.xBall >= 62):
                                    self.ballUp = True
                                    self.xSpeed = 0.1
                                if (self.ballUp == False):
                                    self.yBall += 1
                                else:
                                    self.yBall -= 0.75
                                self.xBall += self.xSpeed
                                self.renderBall()
            
                        if (self.looking == "left"):
                            for i in range(64):
                                self.xBallOffset = -16
                                self.yBallOffset = 20
                                if (self.yBall < -10):
                                    self.ballUp = False
                                if (self.xBall <= -62):
                                    self.ballUp = True
                                    self.xSpeed = 0.1
                                if (self.ballUp == False):
                                    self.yBall += 1
                                else:
                                    self.yBall -= 0.75
                                self.xBall -= self.xSpeed
                                self.renderBall()

                        if (self.looking == "up"):
                            for i in range(64):
                                self.xBallOffset = 0
                                self.yBallOffset = -4
                                if (self.yBall < -62):
                                    self.yBall -= 0.1
                                else:
                                    self.yBall -= 2
                                self.renderBall()
                        if (self.looking == "down"):
                            for i in range(64):
                                self.xBallOffset = 0
                                self.yBallOffset = 40
                                if (self.yBall > 62):
                                    self.yBall += 0.1
                                else:
                                    self.yBall += 2
                                self.renderBall()

                        self.gameHandler.activePokemon.allowTick = True
                        self.gameHandler.activePokemon.x = self.xBallOffset + self.x + self.xBall
                        self.gameHandler.activePokemon.y = self.yBallOffset + self.y + self.yBall
                        for i in range(2):
                            self.gameHandler.recentSteps.insert(0, [self.xBallOffset + self.x + self.xBall, self.yBallOffset + self.y + self.yBall])
                            self.gameHandler.recentSteps.pop()
                    elif (keys[self.pygame.K_r]):
                        self.gameHandler.activePokemon.allowTick = False
            else:
                self.pressed = False

    #   Render the ball when throwing it
    def renderBall(self):    
        self.maps.render()
        self.renderPlayer()
        self.display.blit(self.pokeball, (self.xBallOffset + self.x + self.xBall - self.gameHandler.camera.xOffset, 
                                          self.yBallOffset + self.y + self.yBall - self.gameHandler.camera.yOffset))
        self.pygame.display.update()
        
                    
    #   This is where the collision is beeing handled
    def collision(self):
        playerCol = self.pygame.Rect(self.x - 16 + self.xVel, self.y + 24 + self.yVel, 32, 20)
        for tile_object in self.gameHandler.currentMap.objects:
            if self.pygame.Rect(tile_object.x - (self.gameHandler.currentMap.tilewidth / 2), 
                                tile_object.y - (self.gameHandler.currentMap.tileheight / 2), 
                                tile_object.width, tile_object.height).colliderect(playerCol) == True:

                #   If I Collide with a wall object than I will return false and not apply any movement
                if tile_object.name == "wall":
                    return True

                #   If colided with a name then do something, for example goto a house, downstairs, upstairs excetera.
                elif tile_object.name == "home_door_in":
                    self.x = (self.gameHandler.currentMap.tilewidth * 2.5)
                    self.y = (self.gameHandler.currentMap.tileheight * 5.5)
                    self.Transition(True)
                    self.gameHandler.currentMap = self.gameHandler.home_downstairs
                    self.gameHandler.camera.centerCamera(self)
                    self.Transition(False)
                    
                elif tile_object.name == "home_door_out":
                    self.x = (self.gameHandler.currentMap.tilewidth * 14)
                    self.y = (self.gameHandler.currentMap.tileheight * 3)
                    self.Transition(True)
                    self.gameHandler.currentMap = self.gameHandler.pallet_town
                    self.gameHandler.camera.centerCamera(self)
                    self.Transition(False)

                elif tile_object.name == "home_staircase_down":
                    self.x = (self.gameHandler.currentMap.tilewidth * 8.5)
                    self.y = (self.gameHandler.currentMap.tileheight * 1.5)
                    self.Transition(True)
                    self.gameHandler.currentMap = self.gameHandler.home_downstairs
                    self.gameHandler.camera.centerCamera(self)
                    self.Transition(False)

                elif tile_object.name == "home_staircase_up":
                    self.x = (self.gameHandler.currentMap.tilewidth * 9)
                    self.y = (self.gameHandler.currentMap.tileheight * 1.5)
                    self.Transition(True)
                    self.gameHandler.currentMap = self.gameHandler.home_upstairs
                    self.gameHandler.camera.centerCamera(self)
                    self.Transition(False)

                elif tile_object.name == "oak_in":
                    self.x = (self.gameHandler.currentMap.tilewidth * 4.5)
                    self.y = (self.gameHandler.currentMap.tileheight * 6.5)
                    self.Transition(True)
                    self.gameHandler.currentMap = self.gameHandler.professor_oak_home
                    self.gameHandler.camera.centerCamera(self)
                    self.Transition(False)

                elif tile_object.name == "oak_out":
                    self.gameHandler.gotStarterPokemon = False
                    self.x = (self.gameHandler.currentMap.tilewidth * 41)
                    self.y = (self.gameHandler.currentMap.tileheight * 5)
                    self.Transition(True)
                    self.gameHandler.currentMap = self.gameHandler.pallet_town
                    self.gameHandler.camera.centerCamera(self)
                    self.Transition(False)

                elif tile_object.name == "get-starter":
                    keys = self.pygame.key.get_pressed()
                    if keys[self.pygame.K_RETURN]:
                        if (len(self.gameHandler.caughtPokemons) == 0):
                            self.gameHandler.getStarterActive = True
                        else:
                            self.gameHandler.gotStarterPokemon = True
                            self.gameHandler.getStarterActive = False

                elif tile_object.name == "grass":
                    if (self.moved == True):
                        self.moved = False
                        if (random.randint(0, 9) == 0):
                            self.battleTransition()
                            self.gameHandler.battle.initBattle()
                            self.gameHandler.pokemonFight = True
                            print("DUDUDUDUDUDUDU DUDUDUDUDUDUUD FIIIIIGGGGHTHTHTHTHTHT")
                        
                elif tile_object.name == "pallet-town-out":
                    self.x = (self.gameHandler.currentMap.tilewidth * 32.5)
                    self.y = (self.gameHandler.currentMap.tileheight * 29.5)
                    self.Transition(True)
                    self.gameHandler.currentMap = self.gameHandler.arkala_town
                    self.gameHandler.camera.centerCamera(self)
                    self.Transition(False)

                elif tile_object.name == "pallet-town-in":
                    self.x = (self.gameHandler.currentMap.tilewidth * 18.5)
                    self.y = (self.gameHandler.currentMap.tileheight * -0.5)
                    self.Transition(True)
                    self.gameHandler.currentMap = self.gameHandler.pallet_town
                    self.gameHandler.camera.centerCamera(self)
                    self.Transition(False)

        return False
