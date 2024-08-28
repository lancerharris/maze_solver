import window

def main():
    win = window.Window(800, 600)
    point1 = window.Point(100, 100)
    point2 = window.Point(200, 200)
    line = window.Line(point1, point2)
    win.draw_line(line, "red")
    win.wait_for_close()

if __name__ == "__main__":
    main()
