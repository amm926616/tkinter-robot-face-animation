import tkinter as tk 

class Eye: 
	def __init__(self, canvas, x, y):
		self.canvas = canvas
		self.x = x
		self.y = y 
		self.draw_eye()

	def draw_eye(self): 
		self.canvas.create_oval(self.x, self.y, self.x+50, self.y+50, fill="black")



