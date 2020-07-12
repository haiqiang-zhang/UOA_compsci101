from tkinter import *


def main():
    window = Tk()
    window.title("Red and green pattern")
    window.config(background='white')
    window.geometry("250x250+10+20")
    a_canvas = Canvas(window)
    a_canvas.config(background="white")
    a_canvas.pack(fill=BOTH, expand=True)
    draw_grid(a_canvas)
    draw_pattern_in_canvas(a_canvas, 50, 0, 0, 4)
    window.mainloop()


def draw_grid(canvas):
    for row in range(50, 350, 50):
        canvas.create_line(-1, row, 501, row, fill="lightblue")
    for column in range(50, 500, 50):
        canvas.create_line(column, -1, column, 351, fill="lightblue")


def draw_pattern_in_canvas(a_canvas, size, left_hand_side, y_down, n):
    for row in range(1, n + 1):
        x_left = left_hand_side
        for col in range(1, n + 1):
            rect = (x_left + 2, y_down + 2, x_left + size - 2, y_down + size - 2)
            if col >= row:
                a_canvas.create_rectangle(rect, fill="red")
            x_left = x_left + size
        y_down = y_down + size


main()
