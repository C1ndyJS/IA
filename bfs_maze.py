from collections import deque
import random
import turtle


# Funcion generadora de laberintos
def maze_maker(width, height):

    # Variables constantes del laberinto
    WALL = "X"
    PASSAGE = " "
    START = "S"
    END = "E"

    # Lista laberinto
    maze = [[WALL for _ in range(WIDTH)] for _ in range(HEIGHT)]

    
    # Funcion para confirmar si una celda es valida
    def is_valid(x, y):
        return (0 <= x < WIDTH) and (0 <= y < HEIGHT)

    # Funcion recursiva para generar el laberinto
    def generate_maze(x, y):
        maze[y][x] = PASSAGE

        # List of all possible directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + 2 * dx, y + 2 * dy  # Calcular la posicion del vecino
            if is_valid(nx, ny) and maze[ny][nx] == WALL:
                maze[y + dy][x + dx] = PASSAGE  # Eliminar las paredes entre las celdas
                generate_maze(nx, ny)  # Recursivamente visitar el vecino
                maze[0][0] = START

    # Encontrar un punto final (meta) valida
    start_x, start_y = 0, 0
    end_y = WIDTH-1
    end_x = random.randint(1, HEIGHT // 2)
    maze[end_x][end_y] = END

    # Generar el laberinto inidiando desde el punto (0,0)
    generate_maze(start_x, start_y)

    # Imprimir el laberinto
    for row in maze:
        print(" ".join(row))

    return maze


def bfs_solucionador_laberinto(laberinto):


    
    def bfs_laberinto(laberinto, inicio, objetivo):
        # Definir las direcciones posibles para moverse (arriba, abajo, izquierda, derecha).
        direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Tamaño del laberinto.
        filas = len(laberinto)
        columnas = len(laberinto[0])

        # Función para verificar si una posición está dentro del laberinto y es transitable.
        def es_transitable(x, y):
            return 0 <= x < filas and 0 <= y < columnas and laberinto[x][y] != 'X'

        # Inicializar la cola de BFS con la posición de inicio.
        cola = deque([(inicio[0], inicio[1], 0)])  # (fila, columna, distancia)

        # Crear una matriz para marcar las celdas visitadas y guardar el camino.
        visitado = [[False] * columnas for _ in range(filas)]
        camino = [[None] * columnas for _ in range(filas)]
        visitado[inicio[0]][inicio[1]] = True

        while cola:
            x, y, distancia = cola.popleft()

            # Si llegamos al objetivo, reconstruir el camino y devolverlo.
            if (x, y) == objetivo:
                return reconstruir_camino(camino, inicio, objetivo)

            # Explorar las celdas vecinas.
            for dx, dy in direcciones:
                nx, ny = x + dx, y + dy

                if es_transitable(nx, ny) and not visitado[nx][ny]:
                    cola.append((nx, ny, distancia + 1))
                    visitado[nx][ny] = True
                    camino[nx][ny] = (x, y)

        # Si no se pudo llegar al objetivo, devolvemos None.
        return None

    def reconstruir_camino(camino, inicio, objetivo):
        x, y = objetivo
        camino_solucion = []
        while (x, y) != inicio:
            camino_solucion.append((x, y))
            x, y = camino[x][y]
        camino_solucion.append(inicio)
        camino_solucion.reverse()
        return camino_solucion

    # Encontrar las posiciones de inicio y objetivo.
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[fila])):
            if laberinto[fila][columna] == 'S':
                inicio = (fila, columna)
            elif laberinto[fila][columna] == 'E':
                objetivo = (fila, columna)

    # Resolver el laberinto y obtener el camino.
    camino_solucion = bfs_laberinto(laberinto, inicio, objetivo)

    if camino_solucion:
        print("La solución del laberinto es:")
        for x, y in camino_solucion:
            print("--------------")
            laberinto[x] = laberinto[x][:y] + '.' + laberinto[x][y+1:]
            for fila in laberinto:
                print(fila)
    else:
        print("No se pudo encontrar una solución para el laberinto.")




WIDTH = int(input("\nIngrese el ancho del laberinto: "))   # Ancho del laberinto
HEIGHT = int(input("Ingrese el alto del laberinto: "))     # Alto del laberinto

laberinto = maze_maker(WIDTH, HEIGHT)

laberinto_t = []

# Loop para transformar la lista maze
for i in laberinto:
    x = ''.join(i)
    laberinto_t.append(x)

bfs_solucionador_laberinto(laberinto_t)
