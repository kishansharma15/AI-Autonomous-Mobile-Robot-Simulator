import heapq

def heuristic(a,b):

    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(grid,start,goal):

    rows = len(grid)
    cols = len(grid[0])

    open_set = []
    heapq.heappush(open_set,(0,start))

    came_from = {}
    g_score = {start:0}

    while open_set:

        current = heapq.heappop(open_set)[1]

        if current == goal:

            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.reverse()
            return path

        neighbors = [
            (current[0]+1,current[1]),
            (current[0]-1,current[1]),
            (current[0],current[1]+1),
            (current[0],current[1]-1)
        ]

        for n in neighbors:

            if n[0] < 0 or n[1] < 0 or n[0] >= rows or n[1] >= cols:
                continue

            if grid[n[0]][n[1]] == 1:
                continue

            tentative = g_score[current] + 1

            if n not in g_score or tentative < g_score[n]:

                g_score[n] = tentative
                f = tentative + heuristic(n,goal)

                heapq.heappush(open_set,(f,n))
                came_from[n] = current

    return []