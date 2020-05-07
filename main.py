import pygame, os, math
import Player, Entity, Maps, GameHandler, Camera
import GUI, Menu, MenuPykemons, GetStarter, FPSCounter, Battle

#   Sätter en "path" för att arbeta i samma mapp som main.py ligger inom
path = os.path.dirname(__file__)
os.chdir(path)

#   Variablar för pygame startup
screenWidth = 800
screenHeight = 800

#   Basic pygame startup
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pykemon Testing Concept")
clock = pygame.time.Clock()

gameHandler = GameHandler.GameHandler()
gameHandler.pygame = pygame
gameHandler.display = screen
gameHandler.displayHeight = screenHeight
gameHandler.displayWidth = screenWidth
gameHandler.LoadPokemons()

player = Player.Player(gameHandler.currentMap.tilewidth * 3,gameHandler.currentMap.tileheight * 1.5, 16, 20, 1, gameHandler)
gameHandler.player = player
camera = Camera.Camera(gameHandler)
gameHandler.camera = camera
renderMap = Maps.Maps(gameHandler)
menu = Menu.Menu(gameHandler)
menuPykemons = MenuPykemons.MenuPykemons(gameHandler)
getStarter = GetStarter.GetStarter(gameHandler)
fpsCounter = FPSCounter.FPS(gameHandler, clock)
battle = Battle.battle(gameHandler)

#   GameLoopen som håller spelet igång
def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
        
        screen.fill((0, 0, 0))
        if (gameHandler.pokemonFight == False):
            #   Renderar kartan från Maps.py
            renderMap.render()
            #   Renderar alla entities som finns på skärmen efter att kartan har renderats
            for i in range(2):
                for entity in Entity.entities:
                    if (i == entity.layer and entity.allowTick == True):
                        entity.tick()
            menu.tick()
            menuPykemons.tick()
            getStarter.tick()
        else:
            battle.tick()

        #-------------#   DEBUGGING ONLY   #-------------#
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LCTRL]):
            if (pygame.mouse.get_pressed()[0]):
                xPos = pygame.mouse.get_pos()[0] + gameHandler.camera.xOffset
                yPos = pygame.mouse.get_pos()[1] + gameHandler.camera.yOffset
                print("x = " + str(math.floor(xPos / gameHandler.currentMap.tilewidth)) + "\ny = " + str(math.floor(yPos / gameHandler.currentMap.tileheight)))

        fpsCounter.tick()
        pygame.display.flip()
        clock.tick(60)

game_loop()
pygame.quit()
#   Save data in json files on quit
gameHandler.SaveToJson("pokemons.json", gameHandler.pokemons)
gameHandler.SaveToJson("caughtPokemons.json", gameHandler.caughtPokemons)
