from collections import deque
import random

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[self.WALL for _ in range(width)] for _ in range(height)]
        self.start = (0, 0)
        self.end = (width - 1, height - 1)

    WALL = "1"
    PATH = "0"
    START = "S"
    END = "E"

    def is_valid(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def generate(self):
        def generate_recursive(x, y):
            self.grid[y][x] = self.PATH
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            random.shuffle(directions)

            for dx, dy in directions:
                nx, ny = x + 2 * dx, y + 2 * dy
                if self.is_valid(nx, ny) and self.grid[ny][nx] == self.WALL:
                    self.grid[y + dy][x + dx] = self.PATH
                    generate_recursive(nx, ny)

        generate_recursive(0, 0)
        self.grid[0][0] = self.START
        self.grid[self.height - 1][self.width - 1] = self.END

    def print(self):
        for row in self.grid:
            print(" ".join(row))

    def dfs(self):
        def dfs_helper(x, y):
            if (x, y) == self.end:
                return True

            self.visited[y][x] = True

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if self.is_valid(nx, ny) and not self.visited[ny][nx]:
                    if dfs_helper(nx, ny):
                        self.path.append((nx, ny))
                        return True

            return False

        self.visited = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.path = [(self.start[0], self.start[1])]
        if dfs_helper(self.start[0], self.start[1]):
            return True, self.path
        else:
            return False, []

    def bfs(self):
        def bfs_helper():
            queue = deque([self.start])
            visited = set()
            parent = {}

            while queue:
                x, y = queue.popleft()
                if (x, y) == self.end:
                    path = []
                    while (x, y) != self.start:
                        path.append((x, y))
                        x, y = parent[(x, y)]
                    path.append(self.start)
                    path.reverse()
                    return True, path

                visited.add((x, y))

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if self.is_valid(nx, ny) and (nx, ny) not in visited:
                        queue.append((nx, ny))
                        parent[(nx, ny)] = (x, y)

            return False, []

        return bfs_helper()


def main():
    ANCHO = 10
    ALTO = 6

    laberinto = Maze(ANCHO, ALTO)
    laberinto.generate()

    print("Laberinto:")
    laberinto.print()

    print("Inicio:", laberinto.start)
    print("Fin:", laberinto.end)

    found_dfs, path_dfs = laberinto.dfs()
# Resto del código como antes...
    if found_dfs:
        print("Se puede encontrar un camino usando DFS.")
        maze_copy_dfs = [list(row) for row in lab_aux]
        for x, y in path_dfs:
            if maze_copy_dfs[y][x] == Maze.PATH:
                maze_copy_dfs[y][x] = 'X'
        for row in maze_copy_dfs:
            print("".join(row))
    else:
        print("No hay un camino válido usando DFS.")

    if found_bfs:
        print("Se puede encontrar un camino usando BFS.")
        maze_copy_bfs = [list(row) for row in lab_aux]
        for x, y in path_bfs:
            if maze_copy_bfs[y][x] == Maze.PATH:
                maze_copy_bfs[y][x] = 'X'
        for row in maze_copy_bfs:
            print("".join(row))
    else:
        print("No hay un camino válido usando BFS.")

if __name__ == "__main__":
    main()