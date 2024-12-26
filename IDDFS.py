def iddfs(start, depth, goal):
    def dls(node, depth, path, visited):
        if node == goal:
            return path
        if depth == 0:
            return None
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]  
        for dire in directions:
            new_x = dire[0] + node[0]
            new_y = dire[1] + node[1]
            new_node = (new_x, new_y)
            if (
                0 <= new_x < len(grid)
                and 0 <= new_y < len(grid[0])
                and grid[new_x][new_y] == 0
                and new_node not in visited
            ):
                visited.add(new_node)
                result = dls(new_node, depth - 1, path + [new_node], visited)
                if result:
                    return result
        return None

    while True:
        visited = set([start])
        result = dls(start, depth, [start], visited)
        if result:
            return result
        depth += 1


grid = [
    [0, 0, 1, 0, 1, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
]
start = (0, 0)
goal = (9, 9)

print(iddfs(start, 1, goal))
