import random

def random_obstacles(grid, num):

    h = len(grid)
    w = len(grid[0])

    for _ in range(num):

        x = random.randint(0,w-1)
        y = random.randint(0,h-1)

        grid[y][x] = 1

    return grid