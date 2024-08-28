import window
import random

def main():
    win = window.Window(800, 600)
    point1 = window.Point(10, 10)
    point2 = window.Point(20, 20)
    point3 = window.Point(30, 30)
    point4 = window.Point(40, 40)
    points = [point1, point2, point3, point4]
    cell1 = window.Cell(point1, point2, win)
    cells = []
    for _ in range(10):
        rand_point1 = random.choice(points)
        rand_point2 = random.choice(points)
        cell = window.Cell(rand_point1, rand_point2, win)
        cells.append(cell)
    for cell in cells:
        cell.draw("black")
    win.wait_for_close()

if __name__ == "__main__":
    main()
