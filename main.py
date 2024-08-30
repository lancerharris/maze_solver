from maze import Maze
from graphics import Window
import sys

def main():
    margin = 50
    num_rows = 40
    num_cols = 40
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    sys.setrecursionlimit(10000)
    maze = Maze(
        margin,
        margin,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        10
    )
    maze.solve()

    win.wait_for_close()

if __name__ == "__main__":
    main()
