#Parcial 1: Punto 2d
#Recomendacion modificar Ancho y Alto
from simpleai.search import SearchProblem, depth_first
import random

# Constantes para las celdas
MURO = "█"
PASILLO = " "
INICIO = "S"
FIN = "E"
CAMINO = "°"

# Función para verificar si una celda es válida
def es_valida(x, y):
    return (0 <= x < ANCHO) and (0 <= y < ALTO)

# Función para crear el laberinto y encontrar las coordenadas de inicio y fin
def crear_laberinto(ancho, alto):
    # Inicializa el laberinto como una lista 2D lleno de muros
    laberinto = [[MURO for _ in range(ancho)] for _ in range(alto)]

    # Función recursiva para generar el laberinto utilizando Backtracking
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
        print("".join(fila))
    
    # Encontrar las coordenadas de inicio y fin en el laberinto
    for i in range(alto):
        if FIN in laberinto[i]:
            goal = (laberinto[i].index(FIN), i)
            break  # Romper el bucle una vez que se encuentre la posición de destino
    else:
        # Si no se encuentra 'E' en el laberinto, usar el punto más alejado como destino
        goal = (ancho - 1, alto - 1)

    # Encontrar la posición inicial
    start = (0, 0)

    return laberinto, start, goal

# Definir la clase del problema de búsqueda
class MazeProblem(SearchProblem):
    def __init__(self, initial_state, goal):
        super(MazeProblem, self).__init__(initial_state)
        self.goal = goal

    def is_goal(self, state):
        return state == self.goal

    def actions(self, state):
        actions = []
        x, y = state

        # Definir las acciones posibles (movimientos arriba, abajo, izquierda y derecha)
        possible_moves = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        for move in possible_moves:
            nx, ny = move
            if es_valida(nx, ny) and laberinto[ny][nx] != MURO:
                actions.append(move)

        return actions

    def result(self, state, action):
        return action

    def cost(self, state, action, state2):
        return 1

# Definir las dimensiones del laberinto
ANCHO = 10  
ALTO = 10   

# Crear el laberinto y encontrar las coordenadas de inicio y fin
laberinto, start, goal = crear_laberinto(ANCHO, ALTO)
# Crear una instancia del problema de búsqueda
problem = MazeProblem(start, goal)
# Resolver el laberinto utilizando DFS
result = depth_first(problem)

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
        if laberinto[r][c] != INICIO and laberinto[r][c] != FIN:
            laberinto[r][c] = CAMINO

    # Imprimir el laberinto con el camino marcado
    for row in laberinto:
        print("".join(row))
else:
    print("No se encontró una solución.")