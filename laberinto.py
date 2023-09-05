import random
from simpleai.search import SearchProblem, breadth_first

# Constantes para las celdas
MURO = "X"
PASILLO = " "
INICIO = "S"
FIN = "E"

# Define una clase para representar el problema de búsqueda
class LaberintoProblem(SearchProblem): 
    def __init__(self, grid):
        self.grid = grid
        self.previous_states = {}  # Un diccionario para rastrear los estados anteriores
        super().__init__(initial_state=self.find_start())


    def find_start(self):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == INICIO:
                    return x, y

    def is_goal(self, state):
        x, y = state
        return self.grid[y][x] == FIN

    def actions(self, state):
        x, y = state
        possible_actions = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if (
                0 <= new_x < len(self.grid[0])
                and 0 <= new_y < len(self.grid)
                and self.grid[new_y][new_x] != MURO
            ):
                possible_actions.append((new_x, new_y))
        return possible_actions

    def result(self, state, action):
        return action

    def cost(self, state, action, state2):
        return 1
    
    def register_previous_state(self, state, previous_state):
        self.previous_states[state] = previous_state

    def get_previous_state(self, state):
        return self.previous_states[state]
    
##================================    
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
#===============================================

def resolver_laberinto(laberinto):
    problem = LaberintoProblem(laberinto)

    # Realiza la búsqueda BFS
    result = breadth_first(problem)

    if not result:
        print("No se encontró solución.")
    else:
        # Reconstruir el camino desde el estado final al estado inicial
        current_state = problem.goal
        path = [current_state]
        while current_state != problem.initial_state:
            previous_state = problem.get_previous_state(current_state)
            path.append(previous_state)
            current_state = previous_state

        path.reverse()  # Invierte el camino para que esté en el orden correcto

        # Imprime el camino de la solución
        for y in range(len(laberinto)):
            for x in range(len(laberinto[y])):
                if (x, y) == problem.initial_state:
                    print(INICIO, end=" ")
                elif (x, y) == problem.goal:
                    print(FIN, end=" ")
                elif (x, y) in path:
                    print(".", end=" ")  # Marca el camino con puntos
                else:
                    print(laberinto[y][x], end=" ")
            print()

ANCHO = 4  # Ancho del laberinto
ALTO = 4   # Alto del laberinto
laberinto = crear_laberinto(ANCHO, ALTO)
resolver_laberinto(laberinto)
