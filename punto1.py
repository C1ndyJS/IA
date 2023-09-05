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


# Funcion graficadora de laberintos
def maze_painter(maze):

    # Constants for cells
    WALL = "X"
    PASSAGE = " "
    START = "S"
    END = "E"

    window = turtle.Screen()
    window.bgcolor("grey")
    window.title("LABERINTO")
    t = turtle.Turtle()
    t.fillcolor("green")
    t.speed(-5)
    cell_size = 20

    maze_t = []

    # Loop para transformar la lista maze
    for i in maze:
        x = ''.join(i)
        maze_t.append(x)


    # Function to draw and paint a cell
    def cell_painter(x, y, caracter):
        if caracter == "X":
            turtle.color("black")

        elif caracter == " ":
            turtle.color("white")

        elif caracter == "S":
            turtle.color("yellow")
        
        elif caracter == "E":
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


WIDTH = int(input("Ingrese el ancho del laberinto: "))   # Ancho del laberinto
HEIGHT = int(input("Ingrese el alto del laberinto: "))     # Alto del laberinto
maze = maze_maker(WIDTH, HEIGHT)
maze_painter(maze)

