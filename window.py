from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title("Maze Solver")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas = Canvas(self._root, bg="white", height=height, width=width)
        self._canvas.pack(fill=BOTH, expand=1)
        self._running = False

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._running = True
        while self._running == True:
            self.redraw()
    
    def close(self):
        self._running = False

    def draw_line(self, line, fill_color):
        line.draw(self._canvas, fill_color)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.x1 = point1.x
        self.y1 = point1.y
        self.x2 = point2.x
        self.y2 = point2.y

    def draw(self, canvas, fill_color):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=fill_color, width = 2)

class Cell:
    def __init__(self, top_left_point, bottom_right_point, win):
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