import numpy as np

def slam_update(map_grid,robot_pos):

    x,y = robot_pos

    map_grid[y][x] = 0.5

    return map_grid