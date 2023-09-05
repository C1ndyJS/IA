import heapq
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


# Funcion para resolver el laberinto con A* usando 3 heuristicas
def astar_maze_solver(maze):

    # Función para encontrar la posición de inicio (S) y objetivo (E)
    def find_start_goal(maze):
        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                if cell == 'S':
                    start = (x, y)
                elif cell == 'E':
                    goal = (x, y)
        return start, goal

    start, goal = find_start_goal(maze)

    # Función para encontrar vecinos válidos
    def find_neighbors(pos, maze):
        x, y = pos
        possible_neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        valid_neighbors = []

        for neighbor in possible_neighbors:
            nx, ny = neighbor
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] != 'X':
                valid_neighbors.append(neighbor)

        return valid_neighbors

    # Función para resolver el laberinto usando A* con una heurística
    def astar(maze, start, goal, heuristic):

        open_set = [(0, start)]  # Cola de prioridad (costo, nodo)
        came_from = {}  # Diccionario para rastrear el camino


        # Inicializar g_score con infinito para todas las posiciones válidas en el laberinto
        g_score = {(x, y): float('inf') for x in range(len(maze[0])) for y in range(len(maze)) if maze[y][x] != 'X'}
        g_score[start] = 0

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                return back_home(came_from, current)

            for neighbor in find_neighbors(current, maze):
                tentative_g_score = g_score[current] + 1  # Costo de moverse a un vecino

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))

        return None  # No se encontró un camino

    # Función para reconstruir el camino desde el objetivo hasta el inicio
    def back_home(came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return path[::-1]

    # Heurística 1: Distancia Manhattan
    def heuristic_manhattan(current, goal):
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    # Heurística 2: Distancia Euclidiana
    def heuristic_euclidean(current, goal):
        return ((current[0] - goal[0]) ** 2 + (current[1] - goal[1]) ** 2) ** 0.5

    # Heurística 3: Búsqueda en anchura (sin heurística)
    def straight_line_heuristic(node, goal):
        return max(abs(node[0] - goal[0]), abs(node[1] - goal[1]))

    # Resolver el laberinto usando las tres heurísticas
    path_manhattan = astar(maze, start, goal, heuristic_manhattan)
    path_euclidean = astar(maze, start, goal, heuristic_euclidean)
    path_straight_line = astar(maze, start, goal, straight_line_heuristic)

    # Imprimir los caminos encontrados
    print("\n1. Camino usando distancia Manhattan:")
    print(path_manhattan)

    print("\n2. Camino usando distancia Euclidiana:")
    print(path_euclidean)

    print("\n3. Camino usando Búsqueda en línea recta:")
    print(path_straight_line)

    OPTION = int(input("\nIngrese Heuristica a graficar: "))
    if OPTION == 1:
        path = path_manhattan
    elif OPTION == 2:
        path = path_euclidean
    elif OPTION == 3:
        path = path_straight_line
    else:
        print("ERROR")

    maze = [list(row) for row in maze]
    caracter_camino = 'O'

    # Recorre las coordenadas de solución y modifica el laberinto
    for x, y in path:
        maze[y][x] = caracter_camino


    # Convierte el laberinto de nuevo en una lista de cadenas
    maze_2 = [' '.join(row) for row in maze]
    maze = [''.join(row) for row in maze]

    # Imprime el laberinto con el camino trazado
    print("\n")
    for row in maze_2:
        print(row)
    
    return maze


# Funcion graficadora de laberintos
def maze_painter(maze):

    # Constants for cells
    WALL = "X"
    PASSAGE = " "
    PATH = "O"

    window = turtle.Screen()
    window.bgcolor("grey")
    window.title("LABERINTO")
    t = turtle.Turtle()
    t.speed(-5)
    cell_size = 20

    maze_t = []

    # Loop para transformar la lista maze
    for i in maze:
        x = ''.join(i)
        maze_t.append(x)

    # Function to draw and paint a cell
    def cell_painter(x, y, caracter):
        if caracter == WALL:
            turtle.color("black")

        elif caracter == PASSAGE:
            turtle.color("white")
        
        elif caracter == PATH:
            turtle.color("green")

            
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(cell_size)
            turtle.right(90)
        turtle.end_fill()

    # Bucle para dibujar el laberinto
    for raw, raw_maze in enumerate(maze_t):
        for col, caracter in enumerate(raw_maze):
            x = col * cell_size - len(raw_maze) * cell_size / 2
            y = len(maze_t) * cell_size / 2 - raw * cell_size
            cell_painter(x, y, caracter)

    window.exitonclick()


WIDTH = int(input("\nIngrese el ancho del laberinto: "))   # Ancho del laberinto
HEIGHT = int(input("Ingrese el alto del laberinto: "))     # Alto del laberinto
maze = maze_maker(WIDTH, HEIGHT)
maze_s = astar_maze_solver(maze)
maze_painter(maze_s)

