def avoid_collision(grid,position):

    x,y = position

    if grid[y][x] == 1:
        return False

    return True