import random
from graphics import Line, Point

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                top_left_point = Point(self._x1 + self._cell_size_x * i, self._y1 + self._cell_size_y * j)
                bottom_right_point = Point(self._x1 + self._cell_size_x * (i + 1), self._y1 + self._cell_size_y * (j + 1))
                column.append(Cell(top_left_point, bottom_right_point, self._win))
            self._cells.append(column)
        if self._win:
            for i in range(self._num_cols):
                for j in range(self._num_rows):
                    self._draw_cell(i, j)
        if self._cells:
            self._break_entrance_and_exit()
            self._break_walls_r(0, 0)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        self._cells[i][j].draw("black")
        self._animate() 
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        self._win._root.after(30)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False

        self._draw_cell(0, 0)
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            possible_next_cells = []
            for direction in directions:
                next_i = i + direction[0]
                next_j = j + direction[1]
                if next_i >= 0 and next_i < self._num_cols and next_j >= 0 and next_j < self._num_rows:
                    if not self._cells[next_i][next_j].visited:
                        possible_next_cells.append((next_i, next_j))
            if not possible_next_cells:
                self._draw_cell(i, j)
                break
            next_i, next_j = random.choice(possible_next_cells)
            if i < next_i:
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            elif i > next_i:
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            elif j < next_j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            elif j > next_j:
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            self._draw_cell(i, j)
            self._draw_cell(next_i, next_j)
            self._break_walls_r(next_i, next_j)
        

class Cell:
    def __init__(self, top_left_point, bottom_right_point, win = None):
        self._x1 = top_left_point.x
        self._y1 = top_left_point.y
        self._x2 = bottom_right_point.x
        self._y2 = bottom_right_point.y
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_top_wall = True
        self.visited = False

    def draw(self, fill_color):
        top_left_point = Point(self._x1, self._y1)
        top_right_point = Point(self._x2, self._y1)
        bottom_left_point = Point(self._x1, self._y2)
        bottom_right_point = Point(self._x2, self._y2)

        left_color = fill_color if self.has_left_wall else "white"
        right_color = fill_color if self.has_right_wall else "white"
        top_color = fill_color if self.has_top_wall else "white"
        bottom_color = fill_color if self.has_bottom_wall else "white"

        self._win.draw_line(Line(top_left_point, bottom_left_point), left_color)
        self._win.draw_line(Line(top_right_point, bottom_right_point), right_color)
        self._win.draw_line(Line(top_left_point, top_right_point), top_color)
        self._win.draw_line(Line(bottom_left_point, bottom_right_point), bottom_color)

    def draw_move(self, to_cell, undo=False):
        line_color = "red" if not undo else "gray"
        cell_center = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        to_cell_center = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
        line = Line(cell_center, to_cell_center)
        self._win.draw_line(line, line_color)



