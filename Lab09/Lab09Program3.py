"""
Draws a pattern of red squares and green ovals.
Date-written: Semester 1, 2020.
Author:
"""

from tkinter import *

def main():
    window = Tk()  
    window.title("237994789")   #replace it with your UPI
    window.config(background = 'white')   
    window.geometry("500x350+10+20") 
    a_canvas = Canvas(window) 
    a_canvas.config(background = "white")   
    a_canvas.pack(fill = BOTH, expand = True)
    draw_grid(a_canvas)
    draw_pattern_in_canvas(a_canvas, 4) 
    window.mainloop()

def draw_grid(canvas):
    for row in range(50, 350, 50):
        canvas.create_line(-1, row, 501, row, fill = "lightblue")
    for column in range(50, 500, 50):
        canvas.create_line(column, -1, column, 351, fill = "lightblue")

def draw_pattern_in_canvas(a_canvas, number_of_rows):
    size = 50  #gridsize of 50
    top = 0
    left_hand_side = 0
    for y in range(number_of_rows-1, 0, -1):
        for x in range(y):
            a_canvas.create_rectangle(top+(50*x), left_hand_side, top+(50*x)+size, left_hand_side+size, fill="red")
        left_hand_side += 50
    left_hand_side = 0
    for y in range(1, number_of_rows+1):
        for x in range(y):
            a_canvas.create_oval(top+(50*(number_of_rows-1))-(50*x), left_hand_side, top+(50*(number_of_rows-1))-(50*x)+size, left_hand_side+size, fill="green")
        left_hand_side += 50




            

main()
    

    
            
    
		
    
    
