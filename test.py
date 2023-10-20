import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the window title
root.title("Inclined Arc")

# Create a canvas widget for drawing
canvas = tk.Canvas(root, width=200, height=200, bg="white")
canvas.pack()

# Inclined arc
canvas.create_arc(50, 50, 150, 100, start=0, extent=100, style=tk.ARC, outline="black")

# Start the main event loop
root.mainloop()
