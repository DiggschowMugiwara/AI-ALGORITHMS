

def bfs(q,parent,visited,n,m):

    node = q.pop(0)

    directions = [[-1,0],[1,0],[0,1],[0,-1]]
    for dire in directions:
        new_x = node[0] + dire[0]
        new_y = node[1] + dire[1]
        if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == 0 and (new_x,new_y) not in visited:
            visited.add((new_x,new_y))
            q.append((new_x,new_y))
            parent[(new_x,new_y)] = node

def bidirectional(grid,goal):
    parent_start = {(0,0):None}
    parent_goal = {goal:None}
    n = len(grid)
    m = len(grid[0])
    start_visited = set()
    goal_visited = set()
    start_queue = [(0,0)]
    goal_queue = [goal]
    start_visited.add((0,0))
    goal_visited.add(goal)
    while start_queue and goal_queue:
        bfs(start_queue,parent_start,start_visited,n,m)
        bfs(goal_queue,parent_goal,goal_visited,n,m)
        intersected = None
        for inter_nodes in start_visited:
            if inter_nodes in goal_visited:
                intersected = inter_nodes
                break
        if intersected is not None:
            return reconstruct(intersected,parent_start,parent_goal)
    return None


def reconstruct(intersected,parent,gparent):
    path = []
    curr = intersected
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    curr = intersected
    path.reverse()
    while gparent[curr] is not None:
        curr = gparent[curr]
        path.append(curr) 
    
        
    

    
    return path

    



grid = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

goal = (4, 4)
shortest_path = bidirectional(grid, goal)
if shortest_path:
    print("Shortest Path:", shortest_path)
else:
    print("No Path Found!")

        
    
