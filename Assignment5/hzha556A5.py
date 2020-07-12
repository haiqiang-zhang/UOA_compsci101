'''
Author: Haiqiang Zhang
Username: hzha556
Description: converting palette and pattern file which include decimal number to pixel picture through tkinter and canvas.
'''
from tkinter import *

#-------------------------------------------
#-------------------------------------------
# main() function
#-------------------------------------------
def main():
    size = 50
    start_left = size * 2
    start_down = size * 2
    palette_name = input("Enter a palette filename: ")
    pattern_name = input("Enter a pattern filename: ")
    pattern_list = create_pattern_list(process_file(pattern_name))
    colours_dictionary = create_colours_dict(process_file(palette_name))
    number_of_rows = len(pattern_list)	
    number_of_columns = len(pattern_list[0])
    canvas_width = size * number_of_columns +size * 4
    canvas_height = number_of_rows * size + size * 4
    window = Tk() 
    window.title("A5 by Haiqiang Zhang")
    geometry_string = str(canvas_width)+"x"+str(canvas_height)+"+10+20"
    window.geometry(geometry_string)
    a_canvas = Canvas(window)
    a_canvas.config(background="white")
    a_canvas.pack(fill = BOTH, expand = True) #Canvas fills the whole window  
    draw_pattern(a_canvas, colours_dictionary, pattern_list, size, start_left, start_down)
    window.mainloop()

def split_digits(line):
    line_list = []
    for index in range(len(line)):
        line_list.append(int(line[index]))
    return line_list


def process_file(filename):
    input_file = open(filename, "r")
    file_list = input_file.read().split()
    return file_list
    
def create_colours_dict(lines):
    result_dict = {}
    for index in range(len(lines)):
        left_key = int(lines[index][:1])
        right_value = lines[index][2:]
        result_dict[left_key] = right_value
    return result_dict
    
def create_pattern_list(lines):
    lines_list = []
    for index in range(len(lines)):
        lines_list.append(split_digits(lines[index]))
    return lines_list

def draw_pattern(a_canvas, colours_dictionary, pattern_list, size, left, top):
    possible_digits = "0123456789"      
    down = top
    for index in range(len(pattern_list)):
        for index2 in range(len(pattern_list[index])):
            a_canvas.create_rectangle(left+size*index2, down+size*index, left+size*index2+size, down+size*index+size, fill=colours_dictionary[pattern_list[index][index2]])
    return

main()
