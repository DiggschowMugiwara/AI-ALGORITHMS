def dls(graph,start,depth,goal,visited):
    if depth == 0:
        return False
    if start == goal:
        return True
    visited.add(start)
    directions = [[-1,0],[1,0],[0,-1],[0,1]]
    for dire in directions:
        new_x = start[0] + dire[0]
        new_y = start[1] + dire[1]
        if new_x in range(len(graph)) and new_y in range(len(graph[0])) and (new_x,new_y) not in visited:
            res = dls(graph,(new_x,new_y),depth - 1,goal,visited)
            if res:
                return res
    visited.remove(start)
    return False

graph = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
]
start = (0, 0)
goal = (3, 3)
visited = set()

print(dls(graph, start, 4, goal, visited))
