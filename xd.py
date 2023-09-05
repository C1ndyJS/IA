def dfs(maze, start, end):
    def is_valid(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0
    
    def dfs_helper(x, y):
        if (x, y) == end:
            return True
        
        visited[x][y] = True
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and not visited[nx][ny]:
                if dfs_helper(nx, ny):
                    return True
        
        return False
    
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    return dfs_helper(start[0], start[1])
from collections import deque

def bfs(maze, start, end):
    def is_valid(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0
    
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    queue = deque([(start[0], start[1])])
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return True
        
        visited[x][y] = True
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and not visited[nx][ny]:
                queue.append((nx, ny))
    
    return False

maze = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

if bfs(maze, start, end):
    print("Se puede encontrar un camino usando BFS.")
else:
    print("No hay un camino válido usando BFS.")

maze = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

if dfs(maze, start, end):
    print("Se puede encontrar un camino usando DFS.")
else:
    print("No hay un camino válido usando DFS.")

# Llamado para resolver el laberinto usando BFS
if bfs(maze, start, end):
    print("Se puede encontrar un camino usando BFS.")
else:
    print("No hay un camino válido usando BFS.")