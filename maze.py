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
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
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

    def _draw_cell(self, i, j):
        self._cells[i][j].draw("black")
        if not (i == self._num_cols and j == self._num_rows) and self._win is not None:
            self._animate() 
    
    def _animate(self):
        self._win.redraw()
        self._win._root.after(30)


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

    def draw(self, fill_color):
        top_left_point = Point(self._x1, self._y1)
        top_right_point = Point(self._x2, self._y1)
        bottom_left_point = Point(self._x1, self._y2)
        bottom_right_point = Point(self._x2, self._y2)

        if self.has_left_wall:
            line = Line(top_left_point, bottom_left_point)
            self._win.draw_line(line, fill_color)
        if self.has_right_wall:
            line = Line(top_right_point, bottom_right_point)
            self._win.draw_line(line, fill_color)
        if self.has_top_wall:
            line = Line(top_left_point, top_right_point)
            self._win.draw_line(line, fill_color)
        if self.has_bottom_wall:
            line = Line(bottom_left_point, bottom_right_point)
            self._win.draw_line(line, fill_color)

    def draw_move(self, to_cell, undo=False):
        line_color = "red" if not undo else "gray"
        cell_center = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        to_cell_center = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
        line = Line(cell_center, to_cell_center)
        self._win.draw_line(line, line_color)

