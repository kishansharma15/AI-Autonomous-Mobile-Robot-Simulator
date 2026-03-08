import numpy as np
import random

class GridMap:

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height,width))

    def generate_obstacles(self,count):

        for _ in range(count):

            x = random.randint(0,self.width-1)
            y = random.randint(0,self.height-1)

            self.grid[y][x] = 1