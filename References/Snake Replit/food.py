import random
from snake import Snake

class Food:
    block_size = None
    color = (255, 0, 0, 204)
    x = 240
    y = 400
    bounds = None


    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds


    def draw(self, game, window):
        game.draw.rect(window, self.color, (self.x, self.y, self.block_size, self.block_size))


    def respawn(self):
        self.x = random.randint(100, 380)//10*10
        self.y = random.randint(300, 490)//10*10
