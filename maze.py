from window import Cell, Point


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
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
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw("black")
        if not (i == self._num_cols and j == self._num_rows):
            self._animate() 
    
    def _animate(self):
        self._win.redraw()
        self._win._root.after(30)

