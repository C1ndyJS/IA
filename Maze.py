import random
from simpleai.search import SearchProblem, breadth_first

# Constantes para las celdas
MURO = "X"
PASILLO = " "
INICIO = "S"
FIN = "E"

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


ANCHO = 10  # Ancho del laberinto
ALTO = 10   # Alto del laberinto
laberinto = crear_laberinto(ANCHO, ALTO)
print(laberinto)