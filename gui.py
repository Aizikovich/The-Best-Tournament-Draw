from tkinter import *
from draw import *

def display():
    # Create an instance of tkinter frame
    win = Tk()

    # Set the geometry
    win.geometry("450x280")

    # Create a canvas object
    canvas = Canvas(win, width=1000, height=750, bg="Black")

    # Add a text in Canvas
    teams = "".join(choose_teams(allowed))
    canvas.create_text(230, 150, text=teams, fill="white", font='calibri 20 bold')
    canvas.pack()

    win.mainloop()
    print(teams)
