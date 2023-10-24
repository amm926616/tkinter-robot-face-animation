import customtkinter as tk
from expressionanimation import ExpressionAnimation

root = tk.CTk() 

canvas = tk.CTkCanvas(root, width=600, height=600, background="black")
canvas.pack() 

face = ExpressionAnimation(canvas)
face.blinking()

button = tk.CTkButton(root, text='change expression', command=face.blinking)
button.pack()

root.mainloop()

