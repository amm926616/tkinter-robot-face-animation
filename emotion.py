import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the window title
root.title("Robot Face")

# Create a canvas widget for drawing
canvas = tk.Canvas(root, width=200, height=200, bg="white")
canvas.pack()

# Draw the eyes
canvas.create_oval(60, 40, 80, 60, fill="black")  # Left eye
canvas.create_oval(120, 40, 140, 60, fill="black")  # Right eye

# Draw the mouth
canvas.create_arc(80, 80, 140, 120, start=0, extent=180, style=tk.ARC)

# Start the main event loop
root.mainloop()
