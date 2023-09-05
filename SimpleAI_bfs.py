#Parcial 1 punto 2c BFS

from simpleai.search import SearchProblem, breadth_first
import random

# Símbolos para el laberinto
MURO = "1"
PASILLO = "0"
INICIO = "S"
FIN = "E"

def crear_laberinto(ancho, alto):
    # Inicializa el laberinto como una lista 2D lleno de muros
    laberinto = [[MURO for _ in range(ancho)] for _ in range(alto)]

    # Generar el laberinto comenzando desde una celda aleatoria
    inicio_x, inicio_y = 0, 0
    fin_x = ancho - 1
    fin_y = random.randint(1, alto // 2)

    # Colocar el símbolo 'E' en el punto de destino
    laberinto[fin_y][fin_x] = FIN

    generar_laberinto(laberinto, inicio_x, inicio_y)

    # Imprimir el laberinto
    for fila in laberinto:
        print("".join(fila))
    return laberinto, (inicio_y, inicio_x), (fin_y, fin_x)

def es_valida(x, y, ancho, alto):
    return 0 <= x < ancho and 0 <= y < alto

def generar_laberinto(laberinto, inicio_x, inicio_y):
    stack = [(inicio_x, inicio_y)]

    while stack:
        x, y = stack[-1]  # Obtener la última posición de la pila
        laberinto[y][x] = PASILLO

        # Obtener las celdas vecinas no visitadas
        vecinas = []

        for dx, dy in [(2, 0), (-2, 0), (0, 2), (0, -2)]:
            nx, ny = x + dx, y + dy
            if es_valida(nx, ny, len(laberinto[0]), len(laberinto)) and laberinto[ny][nx] == MURO:
                vecinas.append((nx, ny))

        if vecinas:
            # Elegir una celda vecina aleatoria
            nx, ny = random.choice(vecinas)
            laberinto[ny][nx] = PASILLO

            # Empujar la nueva celda a la pila
            stack.append((nx, ny))
        else:
            # Si no hay celdas vecinas no visitadas, retroceder en la pila
            stack.pop()

# Crear un laberinto aleatorio
ancho = 10  # Ancho del laberinto
alto = 10   # Alto del laberinto
maze, start, goal = crear_laberinto(ancho, alto)

# Definir la clase del problema de búsqueda
class MazeProblem(SearchProblem):
    def __init__(self, initial_state):
        super(MazeProblem, self).__init__(initial_state)

    def is_goal(self, state):
        return state == goal

    def actions(self, state):
        actions = []
        i, j = state

        # Definir las acciones posibles (movimientos arriba, abajo, izquierda y derecha)
        possible_moves = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

        for move in possible_moves:
            x, y = move
            if 0 <= x < len(maze[0]) and 0 <= y < len(maze) and maze[y][x] != MURO:
                actions.append(move)

        return actions

    def result(self, state, action):
        return action

    def cost(self, state, action, state2):
        return 1

# Encontrar las coordenadas de inicio y fin en el laberinto
start = (0, 0)
for i in range(len(maze)):
  if FIN in maze[i]:
    goal = (maze[-1].index(FIN), len(maze) - 1)
    break
  else:
    goal = (ancho-1, alto-1)
    break

# Crear una instancia del problema de búsqueda
problem = MazeProblem(start)

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
        if maze[r][c] != INICIO and maze[r][c] != FIN:
            maze[r][c] = "*"

    # Imprimir el laberinto con el camino marcado
    for row in maze:
        print("".join(row))
else:
     print("No se encontró una solución.")

