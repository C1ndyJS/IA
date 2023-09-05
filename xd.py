#Utilizando BFS y DFS resolver el algoritmo 
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

maze = [
    "00100",
    "00010",
    "11000",
    "01110",
    "00000"
]

start = (0, 0)
end = (4, 4)
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

#Prueba SimpleAI
'''from simpleai.search import SearchProblem, breadth_first

# Definir el laberinto
maze = [
    "S0100",
    "00010",
    "11000",
    "01110",
    "0000E"
]

# Convertir el laberinto en una lista de listas para facilitar el acceso a los elementos
maze = [list(row) for row in maze]

# Encontrar las coordenadas de inicio y fin en el laberinto
def find_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                start = (i, j)
                return start
    raise ValueError("No se encontró la ubicación de inicio ('S') en el laberinto.")

def find_goal(maze):
    return (len(maze) - 1, maze[-1].index("E"))

# Definir la clase del problema de búsqueda
class MazeProblem(SearchProblem):
    def __init__(self, initial_state, goal_state):
        super(MazeProblem, self).__init__(initial_state)
        self.goal_state = goal_state

    def is_goal(self, state):
        return state == self.goal_state

    def actions(self, state):
        actions = []
        i, j = state

        # Definir las acciones posibles (movimientos arriba, abajo, izquierda y derecha)
        possible_moves = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

        for move in possible_moves:
            if 0 <= move[0] < len(maze) and 0 <= move[1] < len(maze[0]) and maze[move[0]][move[1]] != "1":
                actions.append(move)

        return actions

    def result(self, state, action):
        return action

    def cost(self, state, action, state2):
        return 1

# Encontrar las coordenadas de inicio y fin en el laberinto
start = find_start(maze)
goal = find_goal(maze)
# Crear una instancia del problema de búsqueda
problem = MazeProblem(start, goal)

# Resolver el laberinto utilizando BFS
result = breadth_first(problem)

# Mostrar la solución
if result is not None:
    print("Se encontró una solución:")
    
    # Construir el camino desde el resultado
    path = [result.state]
    while result.parent:
        result = result.parent
        path.append(result.state)
    path.reverse()
    
    # Marcar el camino con "*"
    for r, c in path:
        if maze[r][c] != "S" and maze[r][c] != "E":
            maze[r][c] = "*"

    # Imprimir el laberinto con el camino marcado
    for row in maze:
        print("".join(row))
else:
    print("No se encontró una solución.")
'''