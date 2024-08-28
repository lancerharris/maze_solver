import window
import random

def main():
    win = window.Window(800, 600)
    point1 = window.Point(10, 10)
    point2 = window.Point(100, 100)
    point3 = window.Point(100, 10)
    point4 = window.Point(200, 100)
    point5 = window.Point(200, 10)
    point6 = window.Point(300, 100)
    cell1 = window.Cell(point1, point2, win)
    cell2 = window.Cell(point3, point4, win)
    cell3 = window.Cell(point5, point6, win)
    cell1.draw("black")
    cell2.draw("black")
    cell3.draw("black")
    cell1.draw_move(cell2)
    cell2.draw_move(cell3, undo=True)
    win.wait_for_close()

if __name__ == "__main__":
    main()
