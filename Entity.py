from abc import ABC, abstractmethod

entities = []
class Entity:
    def __init__(self, x, y, width, height, layer, gameHandler):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.layer = layer
        self.xVel = 0
        self.yVel = 0
        self.MoveSpeed = 2
        self.allowTick = False

        self.gameHandler = gameHandler
        self.pygame = gameHandler.pygame
        self.display = gameHandler.display

        entities.append(self)

    @abstractmethod
    def tick(self):
        pass