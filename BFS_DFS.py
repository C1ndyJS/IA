#Utilizando BFS y DFS resolver el algoritmo 
from collections import deque
import random
# Constantes para las celdas
MURO = "1"
PASILLO = "0"
INICIO = "S"
FIN = "E"
#==================================================
#                 CREAR LABERINTO 
#==================================================
def crear_laberinto(ancho, alto):
    # Inicializa el laberinto como una lista 2D lleno de muros
    laberinto = [[MURO for _ in range(ancho)] for _ in range(alto)]

    # Función para verificar si una celda es válida
    def es_valida(x, y):
        return (0 <= x < ancho) and (0 <= y < alto)

    # Función recursiva para generar el laberinto utilizando backtracking
    def generar_laberinto(x, y):
        laberinto[y][x] = PASILLO
        # Lista de todas las posibles direcciones
        direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(direcciones)

        for dx, dy in direcciones:
            nx, ny = x + 2 * dx, y + 2 * dy  # Calcular la posición del vecino
            if es_valida(nx, ny) and laberinto[ny][nx] == MURO:
                laberinto[y + dy][x + dx] = PASILLO  # Eliminar la pared entre las celdas
                generar_laberinto(nx, ny)  # Visitar recursivamente al vecino
                laberinto[0][0] = INICIO
            
    # Encontrar un punto de inicio válido y un punto de fin
    inicio_x, inicio_y = 0, 0
    fin_x = ancho - 1
    fin_y = random.randint(1, alto // 2)
    laberinto[fin_y][fin_x] = FIN

    # Generar el laberinto comenzando desde una celda aleatoria
    generar_laberinto(inicio_x, inicio_y)

    # Imprimir el laberinto
    for fila in laberinto:
        print(" ".join(fila))
    return laberinto
#==================================================
#              RESOLVER CON DFS Y BFS 
#==================================================

def is_valid(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[y][x] == PASILLO

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

ANCHO = 10
ALTO = 6

# Llamado a la función para crear el laberinto
laberinto = crear_laberinto(ANCHO, ALTO)

# Transformar el laberinto en una lista de cadenas de caracteres
lab_aux = []
for i in laberinto:
    x = ''.join(i)
    lab_aux.append(x)

print("Laberinto:")
for row in lab_aux:
    print(row)

end = (ANCHO-1,ALTO -1)
start = (0,0)

print(end)
print(type(start), start, end)


#==================================================
# Llamado para resolver el laberinto usando DFS
found_dfs, path_dfs = dfs(lab_aux, start, end)

if found_dfs:
    print("Se puede encontrar un camino usando DFS.")
    # Marcar el camino en el laberinto duplicado
    maze_copy_dfs = [list(row) for row in lab_aux]
    for x, y in path_dfs:
        maze_copy_dfs[x][y] = 'X'  # Usar 'X' para marcar el camino
    for row in maze_copy_dfs:
        print("".join(row))
    print(maze_copy_dfs)
else:
    print("No hay un camino válido usando DFS.")

