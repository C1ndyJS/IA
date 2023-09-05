import random
# Constantes para las celdas
MURO = "█"
PASILLO = " "
INICIO = "S"
FIN = "E"
CAMINO ="°"

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
        print("".join(fila))
    return laberinto


def encontrar_inicio_y_fin(laberinto):
    for y in range(len(laberinto)):
        for x in range(len(laberinto[y])):
            if laberinto[y][x] == INICIO:
                inicio_x, inicio_y = x, y
            elif laberinto[y][x] == FIN:
                fin_x, fin_y = x, y
    return inicio_x, inicio_y, fin_x, fin_y

def resolver_laberinto(laberinto, x, y, fin_x, fin_y):
    if x == fin_x and y == fin_y:
        return True
    if x < 0 or x >= len(laberinto[0]) or y < 0 or y >= len(laberinto):
        return False
    if laberinto[y][x] == MURO:
        return False
    if laberinto[y][x] == CAMINO:
        return False

    laberinto[y][x] = CAMINO

    if (resolver_laberinto(laberinto, x + 1, y, fin_x, fin_y) or
        resolver_laberinto(laberinto, x - 1, y, fin_x, fin_y) or
        resolver_laberinto(laberinto, x, y + 1, fin_x, fin_y) or
        resolver_laberinto(laberinto, x, y - 1, fin_x, fin_y)):
        return True

    laberinto[y][x] = PASILLO
    return False

ANCHO = 20  # Ancho del laberinto
ALTO = 10   # Alto del laberinto
laberinto = crear_laberinto(ANCHO, ALTO)
print("\n")
inicio_x, inicio_y, fin_x, fin_y = encontrar_inicio_y_fin(laberinto)
resolver_laberinto(laberinto, inicio_x, inicio_y, fin_x, fin_y)

# Imprimir el laberinto resuelto
for fila in laberinto:
    print("".join(fila))




