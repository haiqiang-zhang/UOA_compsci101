import tkinter as tk
def draw_pattern(a_canvas, left, top, size):
    number_of_shapes = 3
    for count in range(200):
        colour_fill = "light blue"
        a_canvas.create_line(left+size*count, top, left+size*count, 400000, fill=colour_fill)
        a_canvas.create_line(left, top+size*count, 400000, top+size*count, fill=colour_fill)
    for count in range(number_of_shapes):
        rect = (left, top, left + size, top + size)
        a_canvas.create_rectangle(rect)
        left = left + size
        top = top + size
        size = size + 40

def main():
    window = tk.Tk()
    window.title("my canvas")
    window.geometry("400x400")
    a_canvas = tk.Canvas(window, height=400, width=400)
    a_canvas.config(background="white")
    draw_pattern(a_canvas, 10, 10, 40)
    a_canvas.pack(fill = tk.BOTH, expand = True)
    window.mainloop()

main()