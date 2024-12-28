import heapq
def ucs(graph,start,goal):
    pq = [(0,start)]
    visited = {start:(0,None)}
    while pq:
        (cost,v) = heapq.heappop(pq)
        if v == goal:
            return cost,construct_path(visited,start,goal)
        for nei,cost_nei in graph[v]:
            cost_till = cost + cost_nei
            if nei not in visited or cost_till < visited[nei][0]:
                visited[nei] = (cost_till,v)
                heapq.heappush(pq,(cost_till,nei))
    return None
def construct_path(visited,start,goal):
    curr = goal
    path = []
    while visited[curr][1] is not None:
        path.append(curr)
        curr = visited[curr][1]
    path.reverse()
    return path

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2), ('E', 1)],
    'E': [('B', 5), ('D', 1), ('F', 2)],
    'F': [('C', 3), ('E', 2)]
}

start = 'A'
goal = 'F'

result = ucs(graph, start, goal)

if result:
    cost, path = result
    print(f"Cost: {cost}")
    print(f"Path: {path}")
else:
    print("No path found.")
