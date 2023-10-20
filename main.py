import tkinter as tk 
from eye import Eye

root = tk.Tk() 

canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

left_eye = Eye(canvas, 125, 125)
right_eye = Eye(canvas, 425, 125)

root.mainloop()