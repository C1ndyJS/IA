#Utilizando BFS y DFS resolver el laberinto 
from collections import deque

def is_valid(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == '0'

def dfs(maze, start, end):
    def dfs_helper(x, y):
        if (x, y) == end:
            return True

        visited[x][y] = True

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, maze) and not visited[nx][ny]:
                if dfs_helper(nx, ny):
                    path.append((nx, ny))  # Marcar el camino en la lista 'path'
                    return True
        return False

    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    path = [(start[0], start[1])]  # Iniciar el camino con el punto de inicio
    if dfs_helper(start[0], start[1]):
        return True, path
    else:
        return False, []

def bfs(maze, start, end):
    def bfs_helper(start, end):
        queue = deque([start])
        visited = set()
        parent = {}  # Usar un diccionario para rastrear el camino
        while queue:
            x, y = queue.popleft()
            if (x, y) == end:
                # Reconstruir el camino utilizando el diccionario 'parent'
                path = []
                while (x, y) != start:
                    path.append((x, y))
                    x, y = parent[(x, y)]
                path.append(start)
                path.reverse()
                return True, path
            visited.add((x, y))

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, maze) and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    parent[(nx, ny)] = (x, y)  # Guardar el padre del nodo
        return False, []
    return bfs_helper(start, end)
ANCHO = 4
ALTO = 4
maze = [
    '00100',
    '00010',
    '11000',
    '01110',
    '00000'
]

start = (0, 0)
end = (ANCHO, ALTO)
#==================================================
# Llamado para resolver el laberinto usando DFS
found_dfs, path_dfs = dfs(maze, start, end)

if found_dfs:
    print("Se puede encontrar un camino usando DFS.")
    # Marcar el camino en el laberinto duplicado
    maze_copy_dfs = [list(row) for row in maze]
    for x, y in path_dfs:
        maze_copy_dfs[x][y] = 'X'  # Usar 'X' para marcar el camino
    for row in maze_copy_dfs:
        print("".join(row))
else:
    print("No hay un camino válido usando DFS.")
#==================================================
# Llamado para resolver el laberinto usando BFS
found_bfs, path_bfs = bfs(maze, start, end)

if found_bfs:
    print("Se puede encontrar un camino usando BFS.")
    # Marcar el camino en el laberinto duplicado
    maze_copy_bfs = [list(row) for row in maze]
    for x, y in path_bfs:
        maze_copy_bfs[x][y] = 'X'  # Usar 'X' para marcar el camino
    for row in maze_copy_bfs:
        print("".join(row))
else:
    print("No hay un camino válido usando BFS.")
