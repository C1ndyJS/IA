#Breadth-First Search

from collections import deque
import random
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

def encontrar_inicio_y_fin(laberinto):
    inicio = None
    fin = None
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if laberinto[i][j] == INICIO:
                inicio = (j, i)  # Nota: (x, y) en lugar de (y, x) debido a cómo está definido el laberinto.
            elif laberinto[i][j] == FIN:
                fin = (j, i)
    return inicio, fin

def resolver_laberinto(laberinto):
    inicio, fin = encontrar_inicio_y_fin(laberinto)
    if inicio is None or fin is None:
        return None  # No se encontraron celdas de inicio o fin

    # Inicializamos la cola para el BFS
    cola = deque()
    cola.append((inicio, []))  # Usamos una lista vacía para rastrear el camino

    # Inicializamos un conjunto para mantener un registro de las celdas visitadas
    visitado = set()

    while cola:
        (x, y), camino = cola.popleft()  # Tomamos la celda de la cola
        visitado.add((x, y))  # Marcamos la celda como visitada

        # Verificamos si llegamos a la celda de fin
        if (x, y) == fin:
            return camino + [(x, y)]

        # Exploramos las celdas vecinas
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visitado and laberinto[ny][nx] != MURO:
                cola.append(((nx, ny), camino + [(x, y)]))

    return None  # No se encontró un camino


ANCHO = 10  # Ancho del laberinto
ALTO = 10   # Alto del laberinto
laberinto = crear_laberinto(ANCHO, ALTO)
# Definimos las direcciones posibles (arriba, abajo, izquierda, derecha)
direcciones = [(0, -1), (0, 1), (-1, 0), (1, 0)]
print("\n")
# Resolvemos el laberinto
camino_solucion = resolver_laberinto(laberinto)

if camino_solucion:
    # Marcar el camino en el laberinto
    for x, y in camino_solucion:
        laberinto[y][x] = '1'

    # Imprimir el laberinto con el camino marcado
    for fila in laberinto:
        print(" ".join(fila))
else:
    print("No se encontró un camino desde S hasta E.")
