import random

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
        # blocks_in_x = 300/self.block_size
        # blocks_in_y = 220/self.block_size
        self.x = random.randint(90, 380)//10*10
        self.y = random.randint(300, 500)//10*10
