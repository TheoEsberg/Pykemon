import os, math
path = os.path.dirname(__file__)
os.chdir(path)

import GUI

class FPS(GUI.Gui):
    def __init__(self, gameHandler, clock):
        super().__init__(gameHandler, "fpsCounter")
        self.font = self.pygame.font.Font("fonts/PIXELADE.TTF", 24)
        self.clock = clock

    def tick(self):
        self.fps = self.font.render(str(math.floor(self.clock.get_fps())), True, (255, 0, 0))
        self.display.blit(self.fps, (24, 24))
