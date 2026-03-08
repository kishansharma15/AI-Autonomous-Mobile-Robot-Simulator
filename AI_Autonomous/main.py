from environment.grid_map import GridMap
from robot.mobile_robot import MobileRobot
from navigation.a_star import astar
from simulation.visualization import visualize

def main():

    grid = GridMap(20,20)
    grid.generate_obstacles(40)

    start = (0,0)
    goal = (19,19)

    path = astar(grid.grid,start,goal)

    robot = MobileRobot(start)

    for step in path:
        robot.move(step)

    visualize(grid.grid,path)

if __name__ == "__main__":
    main()