from tkinter import *

width, height = 700, 500
WIN = Tk()
WIN.title("To-Do List")
WIN.geometry(f"{width}x{height}")
num_rows = 1
running = True

def add_row():
    global num_rows
    num_rows += 1
    draw_entries()
    
def draw_entries():
    global num_rows
    for i in range(num_rows):
        Label(WIN, text=f"       {i+1}.").grid(row=i, column=0)
        e1 = Entry(WIN)
        e1.grid(row=i, column=1)
        Button(WIN, text="-").grid(row=i, column=2)
        if i == num_rows-1:
            Button(WIN, text="+", command=add_row).grid(row=i,column = 3)


draw_entries()

WIN.mainloop()